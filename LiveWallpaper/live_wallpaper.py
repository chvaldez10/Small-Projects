import os
import traceback
import ctypes
import time
import cv2

SPI_SETDESKWALLPAPER = 20 # action number to set wallpaper
VIDEO_PATH_PREFIX = r"./assets/video"
IMAGE_PATH_PREFIX = r"./assets/frames"

def get_absolute_path(relative_path):
    # Convert a relative path to an absolute path
    return os.path.abspath(relative_path)

def set_wallpaper(image_path):
    absolute_path = get_absolute_path(image_path)
    print(f"Setting wallpaper: {absolute_path}") 
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, absolute_path, 3)
    if not result:
        print(f"Error setting wallpaper. Last error: {ctypes.GetLastError()}") 

def read_video_frames(video_path):
    absolute_video_path = get_absolute_path(video_path)
    cap = cv2.VideoCapture(absolute_video_path)

    if not cap.isOpened():
        raise IOError("Cannot open video file")

    frame_count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        frame_path = os.path.join(IMAGE_PATH_PREFIX, f'frame_{frame_count}.jpg')
        absolute_frame_path = get_absolute_path(frame_path)
        cv2.imwrite(absolute_frame_path, frame)

        frame_count += 1

    cap.release()
    return frame_count  # Return the total number of frames saved

def set_wallpapers_from_saved_frames(total_frames, frame_rate):
    for frame_count in range(total_frames):
        frame_path = os.path.join(IMAGE_PATH_PREFIX, f'frame_{frame_count}.jpg')
        absolute_frame_path = get_absolute_path(frame_path)
        set_wallpaper(absolute_frame_path)
        time.sleep(1 / frame_rate)
        # break

###########################################################
#
#                        Main loop
#
##########################################################

def main() -> None:
    video_filename = "luffy_gray_terminal.mp4"
    video_path = os.path.join(VIDEO_PATH_PREFIX, video_filename)
    frame_rate = 30

    # total_frames = read_video_frames(video_path)
    total_frames = 696
    set_wallpapers_from_saved_frames(total_frames, frame_rate)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
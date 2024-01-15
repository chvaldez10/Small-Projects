import os
import traceback
import ctypes
import time
import cv2
import tempfile

SPI_SETDESKWALLPAPER = 20  # action number to set wallpaper
VIDEO_PATH_PREFIX = r"./assets/video"

def get_absolute_path(relative_path):
    return os.path.abspath(relative_path)

def set_wallpaper_from_frame(frame):
    with tempfile.NamedTemporaryFile(suffix='.jpg', delete=False) as temp_file:
        cv2.imwrite(temp_file.name, frame)
        temp_file.flush()  # Ensure data is written to disk
        os.fsync(temp_file.fileno())  # Ensure data is written to disk

    absolute_temp_file_path = os.path.abspath(temp_file.name)
    result = ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, absolute_temp_file_path, 3)
    
    if not result:
        print(f"Error setting wallpaper. Last error: {ctypes.GetLastError()}") 
    else:
        # Delete the temporary file after setting the wallpaper
        os.remove(absolute_temp_file_path)

def read_video_frames(video_path):
    absolute_video_path = get_absolute_path(video_path)
    cap = cv2.VideoCapture(absolute_video_path)

    if not cap.isOpened():
        raise IOError("Cannot open video file")

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        yield frame

    cap.release()

def set_wallpapers_from_frames(frame_generator, frame_rate):
    for frame in frame_generator:
        set_wallpaper_from_frame(frame)
        time.sleep(1 / frame_rate)

def main() -> None:
    video_filename = "luffy_gray_terminal.mp4"
    video_path = os.path.join(VIDEO_PATH_PREFIX, video_filename)
    frame_rate = 30

    frame_generator = read_video_frames(video_path)
    set_wallpapers_from_frames(frame_generator, frame_rate)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()

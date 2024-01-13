import os
import traceback
import ctypes
import time

SPI_SETDESKWALLPAPER = 20
VIDEO_PATH_PREFIX = r"./assets/video"

def set_wallpaper(image_path):
    """
    Set the desktop wallpaper to the specified image.

    Args:
    image_path (str): The path to the image file.
    """
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path, 3)

def read_video_frames(video_path):
    pass

def wallpaper_generator(video_path, frame_rate):
    for frame in read_video_frames(video_path):
        yield frame
        time.sleep(1/frame_rate)

###########################################################
#
#                        Main loop
#
##########################################################

def main() -> None:
    video_filename = "luffy_gray_terminal.mp4"
    video_path = os.path.join(VIDEO_PATH_PREFIX, video_filename)
    frame_rate = 30

    while True:
        for frame in read_video_frames(video_path):
            set_wallpaper(frame)
            time.sleep(1 / frame_rate)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}")
        traceback.print_exc()
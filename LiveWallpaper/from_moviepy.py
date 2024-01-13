from moviepy.editor import VideoFileClip
from PIL import Image
import numpy as np
import os
import time

def extract_and_save_frames(video_path, times_to_save):
    video = VideoFileClip(video_path)
    for i, t in enumerate(times_to_save):
        frame = video.get_frame(t)
        frame_path = f'/Users/altonwong/Desktop/LuffyGomu/frame_{i}.jpg'  # Path for each frame
        img = Image.fromarray(frame)
        img.save(frame_path)
        print(f"Frame from {t} seconds saved to {frame_path}")
    video.close()

video_path = 'LuffyGomu.mp4'
video = VideoFileClip(video_path)
video_duration = int(video.duration)
video.close()

# Generate times to save: one frame per second
times_to_save = [i for i in range(video_duration)]  # List of seconds from 0 to duration

extract_and_save_frames(video_path, times_to_save)

def set_wallpaper(image_path):
    script = f'''osascript -e 'tell application "Finder" to set desktop picture to POSIX file "{image_path}"' '''
    os.system(script)
    print("Success")

def cycle_wallpapers(frame_paths, display_time):
    while True:
        for frame_path in frame_paths:
            set_wallpaper(frame_path)
            time.sleep(display_time)

frame_paths = [f'/Users/altonwong/Desktop/LuffyGomu/frame_{i}.jpg' for i in range(len(times_to_save))]
display_time = 0.5

cycle_wallpapers(frame_paths, display_time)
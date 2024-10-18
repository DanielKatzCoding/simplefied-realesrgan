import subprocess
import re
from utils.commander import run


def get_video_fps(video_path):
    try:
        # Run ffmpeg command and capture the output
        result = subprocess.run(['../ffmpeg.exe', '-i', video_path], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        output = result.stderr  # Metadata is in stderr

        # Use regular expression to find FPS
        fps_match = re.search(r"(\d+(?:\.\d+)?) fps", output)
        if fps_match:
            return float(fps_match.group(1))
        else:
            print("FPS information not found.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def extract_video(video_dir, data_dir):
    run(f"ffmpeg -i input_video.mp4 -vf 'fps={get_video_fps(video_dir)}' frames/frame_%04d.png")

import re
import subprocess

from model.paths import Paths
from utils.get_files import get_single_file


class VideoHandler:
    def __init__(self):
        self.video = get_single_file(Paths.video_dir)

    def get_video_fps(self):
        try:
            # Run ffmpeg command and capture the output
            result = subprocess.run([Paths.ffmpeg_path, '-i', self.video],
                                    stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
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

from utils.get_files import get_single_file

from model.video_handler.video_handler import VideoHandler
from utils.commander import run

from model import Paths

class Merge(VideoHandler):
    def __init__(self):
        super().__init__()

    def merge_all(self):
        run(f"\"{Paths.ffmpeg_path}\" -framerate {self.get_video_fps()} "
            f"-i \"{Paths.opt_frames_dir}\\frame_%04d.png\" -i \"{get_single_file(Paths.audio_dir)}\" "
            f"-c:v libx264 -pix_fmt yuv420p -c:a aac -b:a 192k \"{Paths.output_dir}\\output.mp4\"")
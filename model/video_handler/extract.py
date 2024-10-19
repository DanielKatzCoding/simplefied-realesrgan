from model.video_handler.video_handler import VideoHandler
from utils.commander import run

from model import Paths

class Extract(VideoHandler):
    def __init__(self):
        super().__init__()

    def extract_video(self):
        a = f"\"{Paths.ffmpeg_path}\" -i \"{self.video}\" -vf \"fps={self.get_video_fps()}\" \"{Paths.src_frames_dir}\\frame_%04d.png\""
        print(a)
        run(a)

    def extract_audio(self):
        a = f"\"{Paths.ffmpeg_path}\" -i \"{self.video}\" -q:a -map a \"{Paths.audio_dir}\\audio.mp3\""
        run(a)
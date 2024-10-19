from dataclasses import dataclass

@dataclass
class Paths:
    base_path: str
    ffmpeg_path: str
    src_frames_dir: str
    opt_frames_dir: str
    audio_dir: str
    video_dir: str
    output_dir: str
    real_esrgan_path: str

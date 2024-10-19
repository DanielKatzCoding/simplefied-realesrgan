import os

from model import Paths
from utils.commander import run


__all__ = ["highest_enhance"]

def highest_enhance(src_frame: str):
    output_frame = os.path.join(Paths.opt_frames_dir, src_frame := os.path.basename(src_frame))
    run(f"\"{Paths.real_esrgan_path}\" -i \"{Paths.src_frames_dir}\\{src_frame}\" -o \"{output_frame}\" -n realesr-animevideov3-x4")
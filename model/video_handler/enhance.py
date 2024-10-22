import os

from model import Paths
from utils.commander import run


__all__ = ["highest_enhance"]

def highest_enhance():
    run(f"\"{Paths.real_esrgan_path}\" -i \"{Paths.src_frames_dir}\" -o \"{Paths.opt_frames_dir}\" -n realesr-animevideov3-x4",
        void=True)
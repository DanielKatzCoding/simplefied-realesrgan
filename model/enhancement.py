from utils.commander import run
from tqdm import tqdm
import os

class Enhance:
    def __init__(self, src_dir, opt_dir, enhancer_client_path):
        self.src = src_dir
        self.opt = opt_dir
        self.client = enhancer_client_path

    def highest_enhance(self, src_frame):
        output_frame = os.path.join(self.opt, f"frame_{os.path.basename(src_frame)}")
        run(f"{self.client} -i {src_frame} -o {output_frame}\\frame_%04d.png -n realesr-animevideov3-x4")



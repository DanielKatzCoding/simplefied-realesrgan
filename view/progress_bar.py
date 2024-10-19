from tqdm import tqdm
from yt_dlp.utils import frange

from utils.get_files import get_all_files


class ProgressBar:
    def __init__(self, data_dir: str):
        self.frames = get_all_files(data_dir+"\\src_frames")
        self.size = self.frames.qsize()
        self.p_bar = tqdm(total=self.size, desc="Enhancing frames", unit="file")

    def update(self):
        self.p_bar.update(1)  # Update the progress bar for each frame processed

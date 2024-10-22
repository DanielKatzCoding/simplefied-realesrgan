from tqdm import tqdm

from queue import Queue

__all__ = ["ProgressBar"]

class ProgressBar(tqdm):
    __slots__ = []
    def __init__(self, q_frames: Queue[str]):
        super().__init__()
        self.total = q_frames.qsize()
        self.desc = "Enhancing frames"
        self.unit="file"
        self.n = 0
        del q_frames

    def update_static_progress(self, n):
        self.n = n
        self.refresh()

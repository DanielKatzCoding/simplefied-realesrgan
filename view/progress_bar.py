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
        del q_frames

    def update(self, n: float | None = 1):
        super().update(n)  # Call the parent's update method

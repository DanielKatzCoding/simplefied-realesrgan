import os
from tqdm import tqdm

### update to be relevent for controller
def start_all(self):
    frames = sorted(os.listdir(self.src))  # Get the list of frames from source directory
    total_frames = len(frames)

    with tqdm(total=total_frames, desc="Enhancing frames", unit="file") as pbar:
        for frame in frames:
            src_frame_path = os.path.join(self.src, frame)
            self.highest_enhance(src_frame_path)
            pbar.update(1)  # Update the progress bar for each frame processed
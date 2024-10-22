import os
import re
from queue import Queue

BASE_PATH = ""

def get_all_files(directory) -> Queue[str]:
    # List to store the full paths of files
    file_paths = Queue()

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Join the directory path with the file name to get the full path
            full_path = os.path.join(root, file)
            file_paths.put(full_path)

    return file_paths


def get_single_file(directory) -> str:
    # Walk through the directory
    for root, _, files in os.walk(directory):
        if files:  # Check if there are files in the current directory
            # Return the full path of the first file found
            return str(os.path.join(root, files[0]))  # Full path of the first file
    
def get_last_frame_number(dir_path):
    # Pattern to match files named frame_{number}.png
    pattern = re.compile(r'frame_(\d+)\.png')

    frame_number = None
    while not frame_number:
        # Get all files in the directory
        files = os.listdir(dir_path)

        # Extract numbers from the file names
        frame_numbers = []
        for file in files:
            match = pattern.match(file)
            if match:
                frame_numbers.append(int(match.group(1)))

        # If there are no matching files, return None
        if not frame_numbers:
            continue

        # Return the highest number
        return max(frame_numbers)


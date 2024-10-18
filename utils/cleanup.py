import os
import shutil

def clear_directory(dir_path):
    # Check if the directory exists
    if os.path.exists(dir_path) and os.path.isdir(dir_path):
        # Loop through all items in the directory
        for item in os.listdir(dir_path):
            item_path = os.path.join(dir_path, item)
            # Check if it's a file or directory
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.unlink(item_path)  # Remove the file or symbolic link
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)  # Remove the directory and all its contents
    else:
        print(f"The directory {dir_path} does not exist or is not a directory.")


def auto_clear():
    clear_directory("../data/opt_frames")
    clear_directory("../data/src_frames")
    clear_directory("../data/vid")
    clear_directory("../data/audio")

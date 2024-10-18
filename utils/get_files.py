import os


def get_all_files(directory):
    # List to store the full paths of files
    file_paths = []

    # Walk through the directory
    for root, _, files in os.walk(directory):
        for file in files:
            # Join the directory path with the file name to get the full path
            full_path = os.path.join(root, file)
            file_paths.append(full_path)

    return file_paths

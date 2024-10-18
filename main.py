from utils.cleanup import auto_clear
from utils.youtube import download_highest_quality_video
from utils.video_handle import *

import shutil

import os

BASE_PATH = os.getcwd()


def questionare():
    usr_type = input("(youtube url)/local import [(y)/n]: ")
    if usr_type == 'n':
        pth = input("video path: ")
        shutil.copy(pth, f"{BASE_PATH}/vid")

    else:
        pth = input("youtube url: ")
        download_highest_quality_video(pth)
        pth = f"{BASE_PATH}/video.mp4"
    return pth


def main():
    auto_clear()
    pth = questionare()
    fps = get_video_fps(pth)
    separate_video(f"{BASE_PATH}/vid", f"{BASE_PATH}/src_frames", fps)
    extract_audio(f"{BASE_PATH}/vid", f"{BASE_PATH}/audio/audio.mp3")
    enhance_frames(f"{BASE_PATH}/src_frames", f"{BASE_PATH}/opt_frames")
    merge_video(f"{BASE_PATH}/opt_frames", f"{BASE_PATH}/audio/audio.mp3",
                f"{BASE_PATH}/output.mp4", fps)


if __name__ == '__main__':
    main()


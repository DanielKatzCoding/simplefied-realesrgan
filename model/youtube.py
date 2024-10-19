import os
import yt_dlp
from model import Paths


def youtube_download(url):
    # Ensure the directory exists
    if not os.path.exists(Paths.video_dir):
        os.makedirs(Paths.video_dir)

    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio
        'merge_output_format': 'mp4',  # Merge video and audio into MP4
        'outtmpl': f"{Paths.video_dir}/%(title)s.%(ext)s",  # Use video title and extension for temp filename
        'noplaylist': True,  # Do not download playlists if a playlist URL is given
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Download the video
            info_dict = ydl.extract_info(url, download=True)

            # Get the title of the downloaded video
            title = info_dict.get('title', 'video')
            temp_video_path = os.path.join(Paths.video_dir, f"{title}.mp4")
            final_video_path = os.path.join(Paths.video_dir, 'video.mp4')

            # Rename the file to 'video.mp4'
            if os.path.exists(temp_video_path):
                os.rename(temp_video_path, final_video_path)

        return final_video_path  # Return the final filename for further processing
    except Exception as err:
        return {"log": {"error": str(err)}, "run-state": '1'}
import yt_dlp


def download_highest_quality_video(url, ):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio, or best available
        'merge_output_format': 'mp4',  # Merge video and audio into MP4
        'outtmpl': "opt_frames/video.mp4"  # Specify the output path and filename
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


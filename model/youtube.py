import yt_dlp


def youtube_download(url, data_dir):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio, or best available
        'merge_output_format': 'mp4',  # Merge video and audio into MP4
        'outtmpl': data_dir+'\\vid\\video.mp4'  # Specify the output path and filename
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except Exception as err:
        return {"error": err, "run-state": '1'}

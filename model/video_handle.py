import subprocess
import re



def get_video_fps(video_path):
    try:
        # Run ffmpeg command and capture the output
        result = subprocess.run(['../ffmpeg.exe', '-i', video_path], stderr=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        output = result.stderr  # Metadata is in stderr

        # Use regular expression to find FPS
        fps_match = re.search(r"(\d+(?:\.\d+)?) fps", output)
        if fps_match:
            return float(fps_match.group(1))
        else:
            print("FPS information not found.")
            return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def separate_video(input_video, output_frames_dir, fps):
    try:
        # Define the ffmpeg command as a list of arguments
        command = [
            '../ffmpeg.exe',
            '-i', input_video,         # Input video path
            '-qscale:v', '1',          # Set quality scale
            '-vf', f'fps={fps}',           # Set FPS filter to 30
            f'{output_frames_dir}/frame_%04d.png'  # Output frames directory and naming pattern
        ]

        # Run the command
        subprocess.run(command, check=True)
        print("Frames extracted successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def extract_audio(input_video, output_audio):
    try:
        # Define the ffmpeg command as a list of arguments
        command = [
            '../ffmpeg.exe',
            '-i', input_video,  # Input video file
            '-q:a', '0',  # Best audio quality (0 is the best)
            '-map', 'a',  # Extract only the audio stream
            output_audio  # Output audio file (e.g., audio.mp3)
        ]

        # Run the command
        subprocess.run(command, check=True)
        print("Audio extracted successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def enhance_frames(input_directory, output_directory):
    try:
        # Define the command as a list of arguments
        command = [
            '../Real-ESRGA/realesrgan-ncnn-vulkan.exe',  # Path to the Real-ESRGAN executable
            '-i', input_directory,  # Input directory for frames
            '-o', output_directory,  # Output directory for enhanced frames
            '-n', "realesr-animevideov3-x4"  # Model to use for enhancement
        ]

        # Run the command
        subprocess.run(command, check=True)
        print("Frames enhanced successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def merge_video(frames_dir, audio_file, output_video, fps):
    try:
        # Define the ffmpeg command as a list of arguments
        command = [
            '../ffmpeg.exe',
            '-r', f'{fps}',  # Set input frame rate to 30 FPS
            '-i', frames_dir,  # Input image pattern for frames
            '-i', audio_file,  # Input audio file
            '-c:v', 'libx264',  # Video codec
            '-crf', '18',  # Constant Rate Factor for quality
            '-pix_fmt', 'yuv420p',  # Pixel format for compatibility
            '-c:a', 'aac',  # Audio codec
            '-strict', 'experimental',  # Allow experimental codecs
            '-shortest',  # Stop encoding when the shortest input ends
            output_video  # Output video file
        ]

        # Run the command
        subprocess.run(command, check=True)
        print("Video created successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")



import os.path
import shutil
from concurrent.futures import ThreadPoolExecutor, Future
from queue import Queue
from threading import Event
from time import sleep

from model import Paths, youtube_download
from model.video_handler import Extract, EnhanceLib, Merge
from model.intel import Question, Intel
from utils.cleanup import clear_directory
from utils.get_files import get_all_files, get_last_frame_number
from view import Logger, ProgressBar


def set_paths(base_path):
    Paths.base_path = base_path
    Paths.ffmpeg_path = base_path+"\\ffmpeg.exe"
    Paths.real_esrgan_path = base_path+"\\Real-ESRGAN\\realesrgan-ncnn-vulkan.exe"

    Paths.video_dir = base_path+"\\data\\vid"
    Paths.src_frames_dir = base_path+"\\data\\src_frames"
    Paths.opt_frames_dir = base_path+"\\data\\opt_frames"
    Paths.audio_dir = base_path+"\\data\\audio"

    Paths.output_dir = base_path+"\\OUTPUT"


class Controller:
    def __init__(self):
        self.log_queue = Queue()
        self.logger = Logger()

        self.thread_pool = ThreadPoolExecutor()
        self.threads_queue: Queue[Future] = Queue()

        self.e_logger = Event()
        self.e_enhance = Event()

        self.intel = {}

    def start(self):
        self.clear()
        # self.threads_queue.put(self.thread_pool.submit(self.log))
        self.get_intel()
        self.retrieve_video()
        self.extraction()
        self.enhance()
        self.enhance_progress_bar()
        self.merge()

    def _set_output_path(self, output_path):
        if os.path.exists(output_path):
            Paths.output_dir = output_path
            return output_path
        else:
            self.log_queue.put({"log": {"error": "Path Not Found. Changing To Default Path"}})
            return Paths.output_dir

    def _set_ffmpeg_path(self, ffmpeg_path):
        if os.path.exists(ffmpeg_path):
            Paths.ffmpeg_path = ffmpeg_path
            return ffmpeg_path
        else:
            self.log_queue.put({"log": {"error": "Path Not Found. Changing To Default Path"}})
            return Paths.ffmpeg_path

    def log(self):
        while not self.e_logger.is_set():
            if self.log_queue.queue:
                self.logger.add(self.log_queue.get())
            self.logger.print_logs()

    def extraction(self):
        Extract().extract_video()
        Extract().extract_audio()
        self.log_queue.put({"log": {"default": "Done Extracted video and audio"}})

    def enhance_progress_bar(self):
        q_frames = get_all_files(Paths.src_frames_dir)
        pbar = ProgressBar(q_frames)
        while pbar.total > pbar.n:
            pbar.update_static_progress(get_last_frame_number(Paths.opt_frames_dir))
        self.log_queue.put({"log": {"default": "Done Enhancing"}})
        # sleep(10)

    def enhance(self):
        self.threads_queue.put(self.thread_pool.submit(EnhanceLib.highest_enhance))

    def merge(self):
        Merge().merge_all()
        self.log_queue.put({"log": {"default": "Done Merging"}})

    def get_intel(self):
        import_type_q = Question("(1) Youtube Video\n2 Local File\nanswer")
        url_q = Question("Full URL/PATH")
        output_q = Question(f"output path (default: {Paths.output_dir})")
        ffmpeg_q = Question(f"ffmpeg path {('(default: ' + Paths.ffmpeg_path+')') 
        if os.path.exists(Paths.ffmpeg_path) else ''} ")

        intel = Intel()
        intel.add_question("import_type", import_type_q, func=lambda usr: "local" if usr == '2' else 'youtube')
        intel.add_question("url", url_q)
        intel.add_question("output_path", output_q, func=self._set_output_path)
        intel.add_question("ffmpeg_path", ffmpeg_q, func=self._set_ffmpeg_path)
        intel.ask_all()
        self.intel = intel.data
        self.log_queue.put({"log": {"default": "Done Getting data"}})

    def retrieve_video(self):
        try:
            if self.intel["import_type"] == "youtube":
                youtube_download(self.intel["url"])
            elif self.intel["import_type"] == "local":
                shutil.copy(self.intel["url"], Paths.video_dir)
        except Exception as err:
            self.log_queue.put({"log": {"error": f"An unexpected error happened: {err}", "run-state": '1'}})
        self.log_queue.put({"log": {"default": "Done retrieving video"}})


    def clear(self):
        self.log_queue.put(clear_directory(Paths.audio_dir))
        self.log_queue.put(clear_directory(Paths.opt_frames_dir))
        self.log_queue.put(clear_directory(Paths.src_frames_dir))
        self.log_queue.put(clear_directory(Paths.video_dir))
        self.log_queue.put(clear_directory(Paths.output_dir))

    def shutdown(self):
        while self.threads_queue.queue:
            self.thread_pool.shutdown()

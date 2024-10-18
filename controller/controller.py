from threading import Event
from concurrent.futures import ThreadPoolExecutor

from queue import Queue
from utils.commander import run

from utils.cleanup import clear_directory
from view.logger import Logger

class Controller:
    def __init__(self, base_path, data_dir, ffmpeg_path, real_esrgan_path):
        self.base_path = base_path
        self.data_dir = base_path + data_dir
        self.ffmpeg_path = base_path + ffmpeg_path
        self.real_esrgan_path = base_path + real_esrgan_path

        self.log_queue = Queue()
        self.logger = Logger()

        self.thread_pool = ThreadPoolExecutor()
        self.threads_queue = Queue()

        self.e_logger = Event()


    def start(self):
        self.clear()
        self.threads_queue.put(self.thread_pool.submit(self.log))



    def log(self):
        while not self.e_logger.is_set():
            if self.log_queue.not_empty:
                self.logger.add(self.log_queue.get())


    def clear(self):
        self.log_queue.put(clear_directory(self.data_dir+"\\audio"))
        self.log_queue.put(clear_directory(self.data_dir+"\\opt_frames"))
        self.log_queue.put(clear_directory(self.data_dir+"\\src_frames"))
        self.log_queue.put(clear_directory(self.data_dir+"\\vid"))

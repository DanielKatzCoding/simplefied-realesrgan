from threading import Event
from concurrent.futures import ThreadPoolExecutor
from model.paths import Paths

from queue import Queue
from utils.commander import run

from utils.cleanup import clear_directory
from view.logger import Logger

class Controller:
    def __init__(self):
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
        self.log_queue.put(clear_directory(Paths.audio_dir))
        self.log_queue.put(clear_directory(Paths.opt_frames_dir))
        self.log_queue.put(clear_directory(Paths.src_frames_dir))
        self.log_queue.put(clear_directory(Paths.video_dir))
        self.log_queue.put(clear_directory(Paths.output_dir))

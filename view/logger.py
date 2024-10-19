from utils.exceptions import ForceExit

import logging
from queue import Queue
from typing import Dict

class Logger:
    """
    run-state 0=OK - default; 1=ForceExit
    """
    def __init__(self):
        self.q_logs: Queue[Dict[str]] = Queue()
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def add(self, log):
        self.q_logs.put(log)

    def print_logs(self):
        if self.q_logs.queue:
            log = self.q_logs.get_nowait()
            log_msg: Dict[str] = log.get("log")
            if log_msg.get("default"):
                logging.info(log_msg.get("default"))
            elif log_msg.get("error"):
                if log.get("run-state") == '1':
                    logging.critical(log_msg.get("error"))
                    raise ForceExit(log_msg.get("error"))
                else:
                    logging.warning(log_msg.get("error"))

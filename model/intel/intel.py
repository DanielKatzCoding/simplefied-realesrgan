from queue import Queue

from model.intel.question import Question
from types import SimpleNamespace

from typing import Callable, Optional


class Intel:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Intel, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.data = {}
        self.q_questions: Queue[SimpleNamespace] = Queue()

    def add_question(self, keyname: str, question: Question, *, func: Optional[Callable] = None):
        kwargs = SimpleNamespace(**{"keyname": keyname, "question": question, "func": func})
        self.q_questions.put(kwargs)

    def ask_all(self):
        while self.q_questions.queue:
            q = self.q_questions.get()
            opt = input(q.question)
            if q.func:
                opt = q.func(opt)
            self.data[q.keyname] = opt

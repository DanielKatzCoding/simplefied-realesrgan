from sub_intel.question import Question


class Intel:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Intel, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.intel = {}

    def ask(self, keyname:str, question: Question):
        opt = input(question.q)
        self.intel[keyname] = opt

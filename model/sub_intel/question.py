
class Question:
    def __init__(self, q: str, *, prefix: str = "", postfix: str = ": "):
        self.q = prefix+q+postfix

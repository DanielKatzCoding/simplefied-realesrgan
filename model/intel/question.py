class Question:
    def __init__(self, q: str, *, prefix: str = "", postfix: str = ": "):
        self.q = prefix+q+postfix
    def __str__(self):
        return self.q

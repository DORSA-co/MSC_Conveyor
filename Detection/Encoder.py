class Encoder:
    def __init__(self):
        self.line_idx = -1
        self.x = -1
        self.step = 8

    def counter(self):
        self.x += self.step
        self.line_idx += self.step

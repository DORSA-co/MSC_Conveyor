class Encoder:
    def __init__(self):
        self.line_idx = -1
        self.x = -1
        self.step = 8
        self.end_line_idx = 0

    def counter(self):
        self.x += self.step
        self.line_idx += self.step

        if self.line_idx> 985 * 8:
            self.end_line_idx = self.line_idx
            self.line_idx = 0
            self.x = 0
        
        

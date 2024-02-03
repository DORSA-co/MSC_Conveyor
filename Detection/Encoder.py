class Encoder:
    def __init__(self):
        self.line_idx = -1
        self.x = -1
        self.step = 8
        self.end_line_idx = 0
        self.external_finish_event_func = None

    def counter(self):

        self.step = 8
        self.x += self.step
        self.line_idx += self.step

        if self.line_idx> 985 * 8:
            self.end_line_idx = self.line_idx
            self.line_idx = 0
            self.x = 0
            # self.step = 0
            #event
            self.external_finish_event_func(self.end_line_idx)
    

    def set_finish_event(self,func):
        self.external_finish_event_func = func

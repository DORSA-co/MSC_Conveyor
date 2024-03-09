import time

class Encoder:
    SPEED = 300
    def __init__(self):
        self.line_idx = -1
        self.x = -1
        self.step = 0
        self.end_line_idx = 0
        self.external_finish_event_func = None
        self.update_time = None

        self.test_idx= 0

    def counter(self):
        #print(self.step)
        now = time.time()
        if self.update_time is not None:
            self.step = (now - self.update_time) * self.SPEED

        self.test_idx+=1
        #-----------------------
        #self.step = 6
        #-----------------------
        self.update_time = now
        self.x += self.step
        self.line_idx += self.step

        if self.test_idx> 414:
            self.end_line_idx = self.line_idx
            self.line_idx = 0
            self.x = 0
            self.test_idx = 0
            # self.step = 0
            #event
            self.external_finish_event_func(self.get_end_line_idx())
    

    def set_finish_event(self,func):
        self.external_finish_event_func = func

    def get_line_idx(self,):
        return int(self.line_idx)
    
    def get_end_line_idx(self,):
        return int(self.end_line_idx)
    
    def get_step(self,):
        return int(self.step)
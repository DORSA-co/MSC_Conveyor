from Detection.laserScanner import laserScanner
import numpy as np




class beltInspection:

    def __init__(self, kwargs:dict) -> None:
        self.kwargs = kwargs
        self.Scanner = laserScanner()

    
    def change_settings(self, kwargs:dict):
        self.kwargs = kwargs

    

    def feed(self, image:np.ndarray):
        self.current_pts = self.Scanner.laserExtraction(image,
                                     thresh=self.kwargs['background_thresh'],
                                      win_size=self.kwargs['conv_window_size'] )
    

import sys
import os

import numpy as np
import cv2
import time

if __name__ == "__main__":
    sys.path.append(os.getcwd())

from Detection.laserScanner import laserScanner
from Detection.AnomalyDetection import AnomalyDetectionHandeler, ANOMALY_ALGORITHMS
from Detection.DefectExtractor import DefectExtractor
from Detection.ImageCreator import ImageCreator


class beltInspection:

    def __init__(self, kwargs:dict) -> None:
        self.kwargs = kwargs
        # self.kwargs['defect_min_width'] = 2
        self.LaserScanner = laserScanner()
        self.AnomalyDetection = AnomalyDetectionHandeler()
        self.DefectExtractor = DefectExtractor()
        self.ImageCreator = ImageCreator((640,1000), 
                                         step=2, 
                                         max_y_errors=10 )
    
    
    def change_settings(self, kwargs:dict):
        self.kwargs = kwargs

    

    def feed(self, image:np.ndarray):
        self.laser_pts = self.LaserScanner.laserExtraction(image,
                                     thresh=self.kwargs['background_thresh'],
                                      win_size=self.kwargs['conv_window_size'] )
        
        # detect start and stop points

        self.anomaly_pts = self.AnomalyDetection.feed(self.laser_pts, 
                                   diff_thresh=self.kwargs['diff_thresh'],
                                   algorithm=self.kwargs['anomaly_algorithm']
        )
        
        t = time.time()
        self.defect_indices = self.DefectExtractor.feed(self.anomaly_pts, min_width=self.kwargs['defect_min_width'])
        print(time.time() - t)

        self.ImageCreator.feed(self.anomaly_pts, 'gray_gradient')



if __name__ == "__main__":
    
    img = cv2.imread('C:\\Users\\amir\\Desktop\\conveyor_monitoring_system\\demo imgs\\Basler_acA640-300gm__23287291__20231223_170443566_0164.bmp',0)
    kwargs = {
        'background_thresh': 25,
        'conv_window_size': 10,
        'diff_thresh': 2,
        'anomaly_algorithm': ANOMALY_ALGORITHMS.LINE_FIT

    }
    ls = beltInspection(kwargs=kwargs)
    res = np.zeros( img.shape + (3,), dtype=np.uint8)
    ls.feed(img)

    res = ls.LaserScanner.draw(res)
    res =  ls.AnomalyDetection.LineFit.draw(res)

    cv2.imshow('res', res)
    cv2.waitKey(0)
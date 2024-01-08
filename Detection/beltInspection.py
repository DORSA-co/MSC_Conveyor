
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
from Detection.Encoder import Encoder
from Detection.DefectTracker import DefectTracker


class beltInspection:

    def __init__(self, kwargs:dict) -> None:
        self.kwargs = kwargs
        # self.kwargs['defect_min_width'] = 2
        self.LaserScanner = laserScanner()
        self.AnomalyDetection = AnomalyDetectionHandeler()
        self.DefectExtractor = DefectExtractor()
        self.Encoder = Encoder()
        self.DefectTracker = DefectTracker(min_frame_gap=self.Encoder.step*10, min_length=5)
        self.ImageCreator = ImageCreator((640,1000),
                                         max_y_errors=10 )
    
    
    def change_settings(self, kwargs:dict):
        self.kwargs = kwargs

    

    def feed(self, image:np.ndarray):
        t = time.time()

        # SHOULD BE CHANGED
        self.Encoder.counter()
        # SHOULD BE CHANGED

        self.laser_pts = self.LaserScanner.laserExtraction(image,
                                     thresh=self.kwargs['background_thresh'],
                                      win_size=self.kwargs['conv_window_size'] )
        
        # detect start and stop points

        self.anomaly_pts = self.AnomalyDetection.feed(self.laser_pts, 
                                   diff_thresh=self.kwargs['diff_thresh'],
                                   algorithm=self.kwargs['anomaly_algorithm']
        )
        
        self.defect_indices = self.DefectExtractor.feed(self.anomaly_pts, min_width=self.kwargs['defect_min_width'])

        self.DefectTracker.feed(self.defect_indices, self.anomaly_pts[:, 1], self.Encoder.line_idx)
        self.DefectTracker.check_defects_completion(self.Encoder.line_idx)

        image = self.ImageCreator.feed(self.anomaly_pts, 'color_gradient', self.Encoder.step)
        blure_image = cv2.blur(image, ksize=(5, 5))
        res_image = self.DefectTracker.draw(blure_image.copy(), self.Encoder.line_idx)

        print(time.time() - t)

        cv2.imshow('', res_image)

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
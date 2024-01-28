
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
from Detection.Defect import Defect

class beltInspection:

    def __init__(self, kwargs:dict) -> None:
        self.kwargs = kwargs
        self.LaserScanner = laserScanner()
        self.AnomalyDetection = AnomalyDetectionHandeler()
        self.DefectExtractor = DefectExtractor()
        self.Encoder = Encoder()
        self.DefectTracker = DefectTracker(min_frame_gap=self.Encoder.step*10, min_length=5)
        self.ImageCreator = ImageCreator((640, 1000),
                                         max_y_errors=10 )
    
        self.new_defect_event_func = None

        self.DefectTracker.set_new_defect_event(self.new_defect_happend)

    def set_new_defect_event(self, func):
        self.new_defect_event_func = func

    def new_defect_happend(self, defect:Defect):
        """this function call from DefectTracker when new defect occur
        """
        self.new_defect_event_func(defect)
    
    
    def change_settings(self, kwargs:dict):
        self.kwargs = kwargs

    

    def feed(self, image:np.ndarray):
        t = time.time()

        # SHOULD BE CHANGED
        self.Encoder.counter()
        # SHOULD BE CHANGED
        t = time.time()
        self.laser_pts = self.LaserScanner.laserExtraction(image,
                                     thresh=self.kwargs['background_thresh'],
                                      win_size=self.kwargs['conv_window_size'] ) 
        # print('laser extraction: ', time.time() - t)
        
        # detect start and stop points
        t = time.time()
        self.anomaly_pts = self.AnomalyDetection.feed(self.laser_pts, 
                                   diff_thresh=self.kwargs['diff_thresh'],
                                   algorithm=self.kwargs['anomaly_algorithm']
        )
        # print('anomaly detection: ', time.time() - t)
        
        t = time.time()
        self.defect_indices = self.DefectExtractor.feed(self.anomaly_pts, min_width=self.kwargs['defect_min_width'])
        # print('defect extractor: ', time.time() - t)

        t = time.time()
        self.DefectTracker.feed(self.defect_indices, self.anomaly_pts[:, 1], self.Encoder.line_idx)
        # print('defect tracker: ', time.time() - t)

        t = time.time()
        self.DefectTracker.check_defects_completion(self.Encoder.line_idx)
        # print('check completion: ', time.time() - t)

        t = time.time()
        image = self.ImageCreator.feed(self.anomaly_pts, 'color_gradient', self.Encoder.step)
        # print('image creator: ', time.time() - t)

        t = time.time()
        # blure_image = cv2.blur(image, ksize=(3, 3))
        #--------------------------------------
        print(self.Encoder.line_idx)
        self.DefectTracker.check_defect_passed(line_idx=self.Encoder.line_idx,
                                               img_width=image.shape[1])
        self.res_image = self.DefectTracker.draw(image.copy(), 
                                                 self.Encoder.line_idx,
                                                 self.Encoder.end_line_idx)
        
        # print('last draw: ', time.time() - t)

        # cv2.imshow('', res_image)

    
    def find_defect(self, _id)-> Defect:
        for defect in self.DefectTracker.completed_defects:
            if defect.id == _id:
                return defect

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
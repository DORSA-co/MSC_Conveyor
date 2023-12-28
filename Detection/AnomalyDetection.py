import time 

import numpy as np
from scipy.optimize import curve_fit

from Detection import cvToolsCython
from Detection.mathUtils import mathUtils

class ANOMALY_ALGORITHMS:
    LINE_FIT = 'line_fit'
    CURVE_FIT = 'curve_fit'


class AnomalyDetectionHandeler:
    def __init__(self,) -> None:
        self.LineFit = LineFitAnomalyDetection()
        self.CurveFit = CurveFitAnomalyDetection()
        self.__algorithm = ''


    def feed(self, pts:np.ndarray, diff_thresh:int, algorithm:str):
        self.__algorithm = algorithm

        if algorithm == ANOMALY_ALGORITHMS.LINE_FIT:
            return self.LineFit.feed(pts, diff_thresh)
        
        elif algorithm ==ANOMALY_ALGORITHMS.CURVE_FIT:
            return self.CurveFit.feed(pts, diff_thresh)
        
        else:
            print(f'anomaly {self.__algorithm} algorithm not exist for feed')
        
    def draw(self, image):
        if self.__algorithm == ANOMALY_ALGORITHMS.LINE_FIT:
            image = self.LineFit.draw(image)
        
        elif self.__algorithm == ANOMALY_ALGORITHMS.CURVE_FIT:
            image = self.CurveFit.draw(image)
        
        else:
            print(f'anomaly {self.__algorithm} algorithm not exist for drawing')
      
        return image

class _AnomalyDetection:
    
    def __init__(self) -> None:
        self.error_ys = None
        self.pts = None

    def threshould_errors(self, error_ys:np.ndarray, thresh:int):
        error_ys[abs(error_ys)<thresh] = 0
        return error_ys
    
    def draw(self, image:np.ndarray, color:tuple=(0,0,255)):
        defect_pts = self.pts[self.error_ys>0]
        image[defect_pts[:,1], defect_pts[:,0]] = color
        return image
    


class LineFitAnomalyDetection(_AnomalyDetection):
    
    
    def __init__(self,) -> None:
        super().__init__()
        self.slope = None
        self.intercept = None   
        self.xs = None
        self.pred_ys = None
        self.error_ys = None

    
    def calculate_ys(self, xs:np.ndarray, slope:float, intercept:float):
        ys = xs * slope + intercept
        pred_ys = np.round(ys, decimals=0).astype(np.int32)
        return pred_ys
    
    def draw(self,image: np.ndarray, line_color:tuple=(0,255,0), defect_color:tuple=(0,0,255) ):
        image = super().draw(image, color=defect_color)
        image[self.pred_ys, self.xs] = line_color
        return image


    def feed(self, pts:np.ndarray, diff_thresh:int=2):
        self.pts = pts

        self.slope, self.intercept = mathUtils.linear_regression(pts)

        self.xs = pts[:,0]
        self.pred_ys = self.calculate_ys( pts[:,0], self.slope, self.intercept)

        self.error_ys = self.pred_ys - pts[:,1]

        #threshould errors smaller than diff_thresh into 0
        self.error_ys = self.threshould_errors(self.error_ys, diff_thresh)
        
        return self.error_ys






class CurveFitAnomalyDetection(_AnomalyDetection):
    
    
    def __init__(self,) -> None:
        super().__init__()
        self.curve_parms = np.array([0,0,0])
        self.xs = None
        self.pred_ys = None
        self.error_ys = None

    
    def __curve_function(self, x, a, b, c):
        return a * x**2 + b * x + c
    
    def calculate_ys(self, xs, curve_parms):
        pred_ys = self.__curve_function(xs,  *curve_parms)
        pred_ys = np.round(pred_ys, decimals=0).astype(np.int32)
        return pred_ys
    
    def draw(self,image: np.ndarray, line_color:tuple=(0,255,0), defect_color:tuple=(0,0,255) ):
        image = super().draw(image, color=defect_color)
        image[self.pred_ys, self.xs] = line_color
        return image


    def feed(self, pts:np.ndarray, diff_thresh:int=2):
        self.pts = pts

        self.curve_parms, pcov = curve_fit(self.__curve_function, pts[:,0], pts[:,1], self.curve_parms)

        self.xs = pts[:,0]
        self.pred_ys = self.calculate_ys(self.xs, self.curve_parms)

        self.error_ys = self.pred_ys - pts[:,1]

        #threshould errors smaller than diff_thresh into 0
        self.error_ys = self.threshould_errors(self.error_ys, diff_thresh)
        
        return self.error_ys


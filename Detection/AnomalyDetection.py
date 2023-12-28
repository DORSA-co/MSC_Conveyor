import numpy as np
from Detection import cvToolsCython
from Detection.mathUtils import mathUtils

LINE_FIT = 'line_fit'


class AnomalyDetectionHandeler:
    def __init__(self,) -> None:
        self.LineFit = LineFitAnomalyDetection()


    def feed(self, pts:np.ndarray, diff_thresh:int, algorithm:str):
        if algorithm == LINE_FIT:
            self.LineFit.feed(pts, diff_thresh)

      


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

    
    def calculate_ys(self, slope:float, intercept:float, xs:np.ndarray):
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
        self.pred_ys = self.calculate_ys(self.slope, self.intercept, pts[:,0])

        self.error_ys = self.pred_ys - pts[:,1]

        #threshould errors smaller than diff_thresh into 0
        self.error_ys = self.threshould_errors(self.error_ys, diff_thresh)
        
        return self.error_ys
    

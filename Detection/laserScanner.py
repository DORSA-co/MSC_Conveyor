import numpy as np
from Detection import cvToolsCython


class laserScanner:
    
    
    def __init__(self) -> None:
        self.pts = np.array([])
    
    def draw(self,image:np.ndarray, point_color=(255,255,255)):
        if self.pts.size:
            image[self.pts[:,1], self.pts[:,0]] = point_color
        return image
    
    
    def laserExtraction(self, image, thresh, win_size=10):
        self.pts = cvToolsCython.extract_points_maxwin(image, thresh, win_size)
        return self.pts
import numpy as np
from Detection import cvToolsCython


class laserScanner:
    
    
    def __init__(self) -> None:
        pass
    
    def pts2image(self, pts:np.ndarray, img_shape:tuple):
        if pts is None:
            pts = self.pts
        res = np.zeros(img_shape, dtype=np.uint8)
        res[pts[:,1], pts[:,0]] = 255
        return res
    
    
    def laserExtraction(self, image, thresh, win_size=10):
        self.pts = cvToolsCython.extract_points_maxwin(image, thresh, win_size)
        return self.pts
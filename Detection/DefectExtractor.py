import numpy as np
from Detection import cvToolsCython
from scipy.signal import argrelextrema

def local_maximums(error_ys, min_width):
    """Finds the local maxima in a 1D array of error values."""
    max_width = 15
    defect_counts = 0
    res_defect_indices = np.zeros((error_ys.shape[0], 3), dtype=np.uint8)
    for i in range(error_ys.shape[0]):
        start_idx = -1
        end_idx = -1
        if error_ys[i, 1] >= 2 and error_ys[i, 1] > error_ys[i-1, 1] and error_ys[i, 1] >= error_ys[i+1, 1]:
            a = max(i-max_width, 0)
            b = min(i+max_width+1, error_ys.shape[0])
            for j in range(i, a-1, -1):
                if error_ys[j, 1]==0:
                    start_idx = j
                    break
            if start_idx == -1:
                start_idx = a
            for j in range(i, b, 1):
                if error_ys[j, 1]==0:
                    end_idx = j
                    break
            if end_idx == -1:
                end_idx = b
            
            if (end_idx - start_idx) > min_width:
                res_defect_indices[defect_counts, 0] = start_idx
                res_defect_indices[defect_counts, 1] = end_idx
                res_defect_indices[defect_counts, 2] = 0
                defect_counts += 1
    
    return res_defect_indices[:defect_counts]

class DefectExtractor:
    def __init__(self) -> None:
        pass

    def feed(self, error_ys:np.ndarray, min_width:int):
        self.error_ys = error_ys
        self.defect_indices = cvToolsCython.extract_defects(self.error_ys, min_width)
        # self.defect_indices = local_maximums(self.error_ys, min_width)

        return self.defect_indices

    def draw(self, image: np.ndarray, line_color:tuple=(0,255,0)):
        image[:, self.defect_indices[:, 0]] = line_color
        image[:, self.defect_indices[:, 1]] = line_color

        return image
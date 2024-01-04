import numpy as np
from Detection import cvToolsCython

class DefectExtractor:
    def __init__(self) -> None:
        pass

    def feed(self, error_ys:np.ndarray, min_width:int):
        self.error_ys = error_ys
        self.defect_indices = cvToolsCython.extract_defects(self.error_ys, min_width)

    def draw(self, image: np.ndarray, line_color:tuple=(0,255,0)):
        image[:, self.defect_indices[:, 0]] = line_color
        image[:, self.defect_indices[:, 1]] = line_color

        return image
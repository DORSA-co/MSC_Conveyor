import numpy as np
import cv2

from Detection.Defect import Defect

class DefectTracker:
    def __init__(self, min_frame_gap, min_length) -> None:
        self.completed_defects: list[Defect] = []
        self.non_completed_defects: list[Defect] = []

        self.min_frame_gap = min_frame_gap
        self.min_length = min_length

    def set_min_frame_gap(self, min_frame_gap):
        self.min_frame_gap = min_frame_gap

    def set_min_length(self, min_length):
        self.min_length = min_length

    def feed(self, defect_indices: np.ndarray, error_ys: np.ndarray, line_idx: int):
        for defect_index in defect_indices:
            start_idx, end_idx, defect_type = defect_index
            find_defect_flag = False

            depthes_line = error_ys[start_idx:end_idx]

            for non_complete_defect in self.non_completed_defects:
                if non_complete_defect.is_part_of(start_idx, end_idx):
                    find_defect_flag = True
                    non_complete_defect.append_line(start_idx, end_idx, depthes_line, line_idx)
                else:
                    if find_defect_flag:
                        break
            
            if not find_defect_flag:
                new_defect = Defect(
                    start_anomaly_idx=start_idx,
                    end_anomaly_idx=end_idx,
                    depthes=depthes_line,
                    start_line_idx=line_idx
                )

                self.non_completed_defects.append(new_defect)

    def check_defects_completion(self, line_idx):
        i = 0
        while i<len(self.non_completed_defects): 
            defect = self.non_completed_defects[i]
            if defect.is_complete(line_idx, self.min_frame_gap):
                self.non_completed_defects.remove(defect)
                if defect.is_defect(self.min_length):
                    self.completed_defects.append(defect)
            
            else:
                i+=1

    def draw(self, image: np.ndarray, line_idx: int, color: tuple = (33, 33, 133)):
        h, w = image.shape[:2]
        for defect in self.non_completed_defects + self.completed_defects:
            pt1, pt2 = defect.get_bounding_box(line_idx)

            if pt1[0] > w:
                continue

            if not defect.is_defect(self.min_length):
                continue

            image = cv2.rectangle(image, pt1, pt2, color=color, thickness=2)

        return image

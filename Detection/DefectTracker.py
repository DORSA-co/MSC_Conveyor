import numpy as np
import cv2

from Detection.Defect import Defect

class DefectTracker:
    def __init__(self, min_frame_gap, min_length) -> None:
        self.completed_defects: list[Defect] = []
        self.non_completed_defects: list[Defect] = []

        self.min_frame_gap = min_frame_gap
        self.min_length = min_length

        self.external_new_defect_event = None
    
    def set_new_defect_event(self, func):
        self.external_new_defect_event = func

    def set_min_frame_gap(self, min_frame_gap):
        self.min_frame_gap = min_frame_gap

    def set_min_length(self, min_length):
        self.min_length = min_length

    def feed(self, defect_indices: np.ndarray, error_ys: np.ndarray, line_idx: int):
        for defect_index in defect_indices:
            start_idx, end_idx, defect_type = defect_index
            find_defect_flag = False

            updated_defects_id = []
            for defect_id in range(len(self.non_completed_defects)):

                non_complete_defect = self.non_completed_defects[defect_id]

                if non_complete_defect.is_part_of(start_idx, end_idx):
                    find_defect_flag = True
                    non_complete_defect.append_temp_indices(start_idx, end_idx)
                    updated_defects_id.append(defect_id)
                else:
                    if find_defect_flag:
                        break

            #check if multi defects update with same idices merge them    
            if len(updated_defects_id)>1:
                merge_defect = None
                #check from end to start beacuse after delete, other defect id not change
                updated_defects_id.reverse()
                for defect_id in updated_defects_id:
                    merge_defect  = self.non_completed_defects[defect_id] + merge_defect                  
                    self.non_completed_defects.pop(defect_id)
                
                self.non_completed_defects.append(merge_defect)
            
            
            if not find_defect_flag:
                new_defect = Defect(
                    start_anomaly_idx=start_idx,
                    end_anomaly_idx=end_idx,
                    depthes=error_ys,
                    start_line_idx=line_idx
                )

                self.non_completed_defects.append(new_defect)

        for non_complete_defect in self.non_completed_defects:
            non_complete_defect.render(error_ys, line_idx=line_idx)

    def check_defects_completion(self, line_idx):
        i = 0
        while i<len(self.non_completed_defects): 
            defect = self.non_completed_defects[i]
            if defect.is_complete(line_idx, self.min_frame_gap):
                self.non_completed_defects.remove(defect)
                if defect.is_defect(self.min_length):
                    self.completed_defects.append(defect)
                    self.external_new_defect_event(defect)
            
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
    

    

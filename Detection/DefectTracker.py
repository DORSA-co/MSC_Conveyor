import numpy as np
import cv2

from Detection.Defect import Defect
from backend.Utils.idList import idList

class DefectTracker:
    def __init__(self, min_frame_gap, min_length) -> None:
        #self.completed_defects: list[Defect] = []
        #self.non_completed_defects: list[Defect] = []
        #self.__not_pass_completed_defects: list[Defect] = []
        
        self.completed_defects = idList()
        self.non_completed_defects = idList()
        self.__not_pass_completed_defects = idList()
        

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
            for defect_idx in range(len(self.non_completed_defects)):

                non_complete_defect:Defect = self.non_completed_defects[defect_idx]

                if non_complete_defect.is_part_of(start_idx, end_idx):
                    find_defect_flag = True
                    non_complete_defect.append_temp_indices(start_idx, end_idx)
                    updated_defects_id.append(defect_idx)
                else:
                    if find_defect_flag:
                        break

            #check if multi defects update with same idices merge them    
            if len(updated_defects_id)>1:
                merge_defect:Defect = None
                #check from end to start beacuse after delete, other defect id not change
                updated_defects_id.reverse()
                for defect_idx in updated_defects_id:
                    merge_defect  = self.non_completed_defects[defect_idx] + merge_defect                  
                    self.non_completed_defects.remove_by_index(defect_idx)
                
                self.non_completed_defects.append(merge_defect, merge_defect.id)
            
            
            if not find_defect_flag:
                new_defect = Defect(
                    start_anomaly_idx=start_idx,
                    end_anomaly_idx=end_idx,
                    depthes=error_ys,
                    start_line_idx=line_idx
                )

                self.non_completed_defects.append(new_defect, new_defect.id)

        for non_complete_defect in self.non_completed_defects.values():
            non_complete_defect.render(error_ys, line_idx=line_idx)

    def check_defects_completion(self, line_idx):
        i = 0
        while i<len(self.non_completed_defects): 
            defect:Defect = self.non_completed_defects[i]
            if defect.is_complete(line_idx, self.min_frame_gap):
                
                self.non_completed_defects.remove_by_value(defect)
                if defect.is_defect(self.min_length):
                    
                    self.__not_pass_completed_defects.append(defect, defect.id)
                    #------------------------------------
                    #check if defect is update of another defect
                    for i in range(self.completed_defects.count()):
                        if defect.is_same(self.completed_defects[i]):
                            defect.id = self.completed_defects[i].id
                            #self.completed_defects[i] = defect
                            self.completed_defects.set_by_index(i, defect, defect.id)
                            
                            break
                    #------------------------------------
                    else:
                        self.completed_defects.append(defect, defect.id)
                        self.external_new_defect_event(defect)
            
            else:
                i+=1
        
        
    def check_defect_passed(self, line_idx, img_width):
        i  = 0
        while i < len(self.__not_pass_completed_defects):
            if self.__not_pass_completed_defects[i].is_present_in_image(line_idx, img_width):
                i+=1
                continue
            self.__not_pass_completed_defects.remove_by_index(i)


    def draw(self, image: np.ndarray, line_idx: int, end_belt_line_idx:int, color: tuple = (33, 33, 133)):
        h, w = image.shape[:2]

        for defect in self.non_completed_defects.values():
            pt1, pt2 = defect.get_bounding_box(line_idx, end_belt_line_idx)

            if not defect.is_defect(self.min_length):
                continue

            image = cv2.rectangle(image, pt1, pt2, color=color, thickness=2)

        defect:Defect
        for defect in self.__not_pass_completed_defects.values():
            pt1, pt2 = defect.get_bounding_box(line_idx, end_belt_line_idx)

            if pt1[0] > w:
                self.__not_pass_completed_defects.remove_by_value(defect)
                continue


            image = cv2.rectangle(image, pt1, pt2, color=(255,0,0), thickness=2)
        

        
        
        return image
    
    

    

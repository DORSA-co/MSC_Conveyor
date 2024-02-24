import numpy as np
import cv2

from Detection.Defect import Defect
from backend.Utils.idList import idList

class DefectTracker:
    DUBGE = True
    def __init__(self) -> None:
        # self.debug_defects = {
        #     'complete':[],
        #     'non_complete':[],
        #     'not_defect':[],
        #     'precense':[]
        # }
        #self.completed_defects: list[Defect] = []
        #self.non_completed_defects: list[Defect] = []
        #self.__not_pass_completed_defects: list[Defect] = []
        
        self.completed_defects = idList()
        self.non_completed_defects = idList()
        self.__not_pass_completed_defects = idList()

        self.external_new_defect_event = None
        self.external_defect_update_event = None
    
    def set_new_defect_event(self, func):
        self.external_new_defect_event = func
    
    def set_update_defect_event(self, func):
        self.external_defect_update_event = func

    def feed(self, defect_indices: np.ndarray, error_ys: np.ndarray, line_idx: int, belt_end_line_idx):
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
            non_complete_defect.render(error_ys, line_idx)

        
        for i in range(len(self.completed_defects)):
            defect:Defect = self.completed_defects[i]
            defect.update_line_idx(line_idx, belt_end_line_idx)
        
        for i in range(len(self.non_completed_defects)):
            defect:Defect = self.non_completed_defects[i]
            defect.update_line_idx(line_idx, belt_end_line_idx)

    def check_defects_completion(self, min_frame_gap, min_length, line_idx):
        i = 0
        while i<len(self.non_completed_defects): 
            defect:Defect = self.non_completed_defects[i]
            if defect.is_complete(line_idx, min_frame_gap):
                
                self.non_completed_defects.remove_by_value(defect)
                if defect.is_defect(min_length):
                    
                    self.__not_pass_completed_defects.append(defect, defect.id)
                    #------------------------------------
                    #check if defect is update of another defect
                    for i in range(self.completed_defects.count()):
                        if defect.is_same(self.completed_defects[i]):
                            defect.id = self.completed_defects[i].id
                            #self.completed_defects[i] = defect
                            self.completed_defects.set_by_index(i, defect, defect.id)
                            self.external_defect_update_event(defect)
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


    def draw(self, min_length, image: np.ndarray, line_idx: int, color: tuple = (33, 33, 133)):
        #print('total defect to draw',len(self.non_completed_defects) + len(self.__not_pass_completed_defects))
        for defect in self.non_completed_defects.values():

            if not defect.is_defect(min_length):
                continue
            
            image = defect.draw(image, line_idx, color)
            

        defect:Defect
        for defect in self.__not_pass_completed_defects.values():

            # if pt1[0] > w:
            #     self.__not_pass_completed_defects.remove_by_value(defect)
            #     continue

            image = defect.draw(image, line_idx, (0,255,0))
        

        
        
        return image
    
    

    

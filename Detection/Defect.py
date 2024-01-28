from __future__ import annotations

import time

from persiantools.jdatetime import JalaliDate,JalaliDateTime
import numpy as np


class numberStatics:
    def __init__(self):
        self.max = -np.inf
        self.min = np.inf
        self.mean = -1
        self.count = 0

    def add_list(self, values: np.ndarray) -> None:
        self.update_mean(values)
        self.update_max(values)
        self.update_min(values)

    def add(self, value: float) -> None:
        self.update_mean(np.array([value]))
        self.update_max(np.array([value]))
        self.update_min(np.array([value]))

    def update_mean(self, values: np.ndarray) -> None:
        sum = self.mean * self.count + values.sum()
        self.count += values.shape[0]

        self.mean = sum / self.count

    def update_max(self, values: np.ndarray) -> None:
        self.max = max(self.max, values.max())

    def update_min(self, values: np.ndarray) -> None:
        self.min = min(self.min, values.min())

    
    def __add__(self, other:numberStatics):
        res = numberStatics()
        res.max = max(self.max, other.max)
        res.min = min(self.min, other.min)
        res.count = self.count + other.count
        res.mean = (self.mean * self.count + other.mean * other.count) / res.count
        return res




class Defect:
    def __init__(
            self,
            start_anomaly_idx: int,
            end_anomaly_idx: int,
            start_line_idx: int,
            depthes: np.ndarray,
            n_last_defects: int = 3
        ):
        self.id = time.time()
        self.widthInfo = numberStatics()
        self.depthInfo = numberStatics()
        self.jdatetime = JalaliDateTime.now()

        self.n_last_defects = n_last_defects
        self.defect_indices = np.array(([[start_anomaly_idx, end_anomaly_idx]]))
        self.temp_indices = np.array([])

        
        self.start_line_idx = start_line_idx
        self.end_line_idx = self.start_line_idx
        
        self.lenght = 0

        self.defect_width_boundries = (start_anomaly_idx, end_anomaly_idx)
        
        if start_anomaly_idx is not None:
            self.__append_width_info(start_anomaly_idx, end_anomaly_idx)
            self.__append_depth_info(depthes[start_anomaly_idx:end_anomaly_idx])

    
    def append_temp_indices(self, start_anomaly_idx, end_anomaly_idx):
        if self.temp_indices.shape[0]:
            new_row = np.array([[start_anomaly_idx, end_anomaly_idx ]])
            self.temp_indices = np.append( self.temp_indices, new_row, axis=0 )
        else:
            self.temp_indices = np.array(([[start_anomaly_idx, end_anomaly_idx]]))

    def render(self, depthes, line_idx):
        if not self.temp_indices.shape[0]:
            return
        start_anomaly_idx = self.temp_indices[:,0].min()
        end_anomaly_idx = self.temp_indices[:,1].max()
        self.temp_indices = np.array([])

        depthes = depthes[start_anomaly_idx:end_anomaly_idx]

        self.__append_width_info(start_anomaly_idx, end_anomaly_idx)
        self.__append_depth_info(depthes)
        self.__append_idx(start_anomaly_idx, end_anomaly_idx)
        self.end_line_idx = line_idx
        self.defect_width_boundries = (
            min(self.defect_width_boundries[0], start_anomaly_idx),
            max(self.defect_width_boundries[1], end_anomaly_idx)
        )

        self.lenght = self.end_line_idx - self.start_line_idx

    def is_complete(self, line_idx:int, min_idx_gap):
        if line_idx - self.end_line_idx >= min_idx_gap:
            return True
        return False
    
    def is_defect(self, min_length: int):
        if (self.end_line_idx - self.start_line_idx) > min_length:
            return True
        else:
            return False
        
    def is_present_in_image(self,line_idx, img_w):
        x1 = line_idx - self.end_line_idx
        if -img_w< x1 < img_w :
            return True
        return False
    

    def is_part_of(self, start_idx, end_idx, max_distance=20):
        try:
            defect_start_idx = self.defect_indices[:, 0].min()
            defect_end_idx = self.defect_indices[:, 1].max()
        except:
            print(self.defect_indices)

        distance = self.__calc_overlap(start_idx, end_idx,
                            defect_start_idx, defect_end_idx)
        
        if distance > 0:
            return True
        elif np.abs(distance) < max_distance:
            return True 
        else:
            return False
        
    def get_bounding_box(self, line_idx, end_line_idx):
        #when belt pass the end and start from 0 again
        if line_idx < self.end_line_idx:
            x1 = line_idx + (end_line_idx - self.end_line_idx)
            x2 = line_idx + (end_line_idx - self.start_line_idx)
        else:
            x1 = line_idx - self.end_line_idx
            x2 = line_idx - self.start_line_idx

        y1 = self.defect_width_boundries[0]
        y2 = self.defect_width_boundries[1]

        return (x1, y1), (x2, y2)

    def __append_width_info(self, start_idx, end_idx):
        self.widthInfo.add(end_idx - start_idx)

    def __append_depth_info(self, depthes):
        self.depthInfo.add_list(depthes)

    def __append_idx(self, start_idx, end_idx):
        self.defect_indices = np.append( self.defect_indices, np.array([[start_idx, end_idx ]]), axis=0 )
        if len(self.defect_indices) > self.n_last_defects:
            # self.defect_indices = self.defect_indices[-self.n_last_defects]
            self.defect_indices = self.defect_indices[-self.n_last_defects:, :]

    def __calc_overlap(self, s1:int,e1:int , s2:int, e2:int):
        distance = min(e1, e2) - max(s1, s2)

        return distance
    

    def __add__(self, other:Defect):
        if other is None:
            return self
        res_defect = Defect(None,None,None,None)

        res_defect.start_line_idx = min(self.start_line_idx, other.start_line_idx)
        res_defect.end_line_idx = max(self.end_line_idx, other.end_line_idx)
        res_defect.n_last_defects = max(self.n_last_defects, other.n_last_defects)

        res_defect.temp_indices = np.vstack(( self.temp_indices, other.temp_indices ))
        
        #---------------------------------------------
        start_defect_idx = min(self.defect_indices[:,0].min(), other.defect_indices[:,0].min() )
        end_defect_idx = max(self.defect_indices[:,1].max(), other.defect_indices[:,1].max() )
        res_defect.defect_indices = np.array([[start_defect_idx, end_defect_idx]])
        #---------------------------------------------

        

        res_defect.depthInfo = self.depthInfo + other.depthInfo
        res_defect.widthInfo = self.widthInfo + other.widthInfo
        
        start_width_idx = min(self.defect_width_boundries[0], other.defect_width_boundries[0])
        end_width_idx = max(self.defect_width_boundries[1], other.defect_width_boundries[1])

        res_defect.defect_width_boundries = (start_width_idx,end_width_idx)

        
        return res_defect
    
    def is_same(self, other:Defect):
        intersect_y1 = max(self.defect_width_boundries[0], other.defect_width_boundries[0])
        intersect_y2 = min(self.defect_width_boundries[1], other.defect_width_boundries[1])

        if intersect_y2 > intersect_y1:
            intersect_x1 = max(self.start_line_idx, other.start_line_idx)
            intersect_x2 = min(self.end_line_idx, other.end_line_idx)
            if intersect_x2> intersect_x1:
                return True
        return False


    def get_info_for_filter(self,):
        res = {
            'width': (self.widthInfo.min, self.widthInfo.max),
            'depth': (self.depthInfo.min, self.depthInfo.max),
            'lenght': self.lenght,
            'date': self.jdatetime.date(),
        }

        return res
from __future__ import annotations

import time

## DATE ##
#from persiantools.datetime import JalaliDate, JalaliDateTime
from datetime import datetime
# from datetime import datetime
import numpy as np
import cv2

from Constants.Constant import DecimalRound


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
    width_px2mm = 0.3
    depth_px2mm = 0.7
    lenght_px2mm = 3
    def __init__(
            self,
            start_anomaly_idx: int = None,
            end_anomaly_idx: int = None,
            start_line_idx: int = None,
            depthes: np.ndarray = None,
            n_last_lines: int = 3
        ):
        #self.id = int((time.time() - RefernceTime.REFERENCE_TIME)*(10000))
        self.id = id(self)
        self.widthInfo = numberStatics()
        self.depthInfo = numberStatics()
        ## DATE ##
        self.datetime = datetime.now() #datetime.now()

        self.n_last_lines = n_last_lines
        
        self.defect_indices = np.array(([[start_anomaly_idx, end_anomaly_idx]]))
        self.temp_indices = np.array([])

        
        self.start_line_idx = start_line_idx
        self.end_line_idx = self.start_line_idx

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

    def is_same(self, other:Defect):
        intersect_y1 = max(self.defect_width_boundries[0], other.defect_width_boundries[0])
        intersect_y2 = min(self.defect_width_boundries[1], other.defect_width_boundries[1])

        if intersect_y2 > intersect_y1:
            self_end_temp = self.end_line_idx
            other_end_temp = other.end_line_idx 
            
            intersect_x1 = max(self.start_line_idx, other.start_line_idx)
            intersect_x2 = min(self_end_temp, other_end_temp)
            if intersect_x2> intersect_x1:
                return True
        return False

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
        (x1,_), (_,_) = self.get_bounding_box(line_idx)
        if -img_w< x1 < img_w :
            return True
        return False
    

    def is_part_of(self, start_idx, end_idx, max_distance=20):
        try:
            defect_start_idx = self.defect_indices[:, 0].min()
            defect_end_idx = self.defect_indices[:, 1].max()
        except:
            print('Defect is_part_of ERROR:',self.defect_indices)

        distance = self.__calc_overlap(start_idx, end_idx,
                            defect_start_idx, defect_end_idx)
        
        if distance > 0:
            return True
        elif np.abs(distance) < max_distance:
            return True 
        else:
            return False
        
    
        
    def get_bounding_box(self, line_idx, border=12):
        x1 = line_idx - self.end_line_idx
        x2 = line_idx - self.start_line_idx

        y1 = self.defect_width_boundries[0]
        y2 = self.defect_width_boundries[1]

        x1 -=border
        x2 += border
        y1 -= border
        y2 += border

        return (x1, y1), (x2, y2)
    
    def draw(self, image:np.ndarray, line_idx:int, color:tuple=(255,0,0)):
        pt1, pt2 = self.get_bounding_box(line_idx,)
        res = cv2.rectangle(image, pt1, pt2, color=color, thickness=2)
        
        res =  self.__draw_debug(res,pt1,pt2)
        return res
    
    
    def get_length(self):
        lenght_m = abs(self.end_line_idx - self.start_line_idx)/1000 * self.lenght_px2mm
        return np.round(lenght_m, DecimalRound.ROUND_DECIMAL)


    def get_info_for_filter(self,):
        res = {
            'width': (self.widthInfo.min, self.widthInfo.max),
            'depth': (self.depthInfo.min, self.depthInfo.max),
            'lenght': self.get_length(),
            ## DATE ##
            'date': self.datetime.date(),
        }

        return res
    
    def get_info(self, ):
        res = {}
        res['defect_id'] = self.id

        ## DATE ##
        res['date'] = self.datetime.date()
        res['time'] = self.datetime.time()

        res['x'] = self.start_line_idx
        res['y'] = self.defect_width_boundries[0]

        res['min_width'] = np.round(self.widthInfo.min, DecimalRound.ROUND_DECIMAL)
        res['mean_width'] = np.round(self.widthInfo.mean, DecimalRound.ROUND_DECIMAL)
        res['max_width'] = np.round(self.widthInfo.max, DecimalRound.ROUND_DECIMAL)

        res['min_depth'] = np.round(self.depthInfo.min, DecimalRound.ROUND_DECIMAL)
        res['mean_depth'] = np.round(self.depthInfo.mean, DecimalRound.ROUND_DECIMAL)
        res['max_depth'] = np.round(self.depthInfo.max, DecimalRound.ROUND_DECIMAL)

        res['length'] = self.get_length()

        return res
    


    def update_line_idx(self, line_idx, belt_end_line_idx):
        if self.end_line_idx > 0:
            if line_idx < self.end_line_idx :
                self.end_line_idx -= belt_end_line_idx
        
        else:
            if line_idx > self.end_line_idx + belt_end_line_idx:
                self.end_line_idx += belt_end_line_idx

        if self.start_line_idx > 0:
            if line_idx < self.start_line_idx :
                self.start_line_idx -= belt_end_line_idx
        else:
            if line_idx > self.start_line_idx + belt_end_line_idx:
                self.start_line_idx += belt_end_line_idx

    
    def __draw_debug(self, image, pt1, pt2):
        x,y = pt1
        image = cv2.putText(image,
                        text=str(self.id),
                        org=(x,y),
                        fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
                        fontScale=1,
                        color=(0,0,0),
                        thickness=1
                        )
        
        image = cv2.putText(image,
                        text=str((x,y)),
                        org=(x,y-20),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                        fontScale=1,
                        color=(0,0,0),
                        thickness=1
                        )
        return image

    def __append_width_info(self, start_idx, end_idx):
        width_cm = abs(end_idx - start_idx) * self.width_px2mm / 10
        self.widthInfo.add(width_cm)

    def __append_depth_info(self, depthes_px):
        depthes_mm = depthes_px * self.depth_px2mm
        self.depthInfo.add_list(depthes_mm)

    def __append_idx(self, start_idx, end_idx):
        self.defect_indices = np.append( self.defect_indices, np.array([[start_idx, end_idx ]]), axis=0 )
        if len(self.defect_indices) > self.n_last_lines:
            # self.defect_indices = self.defect_indices[-self.n_last_lines]
            self.defect_indices = self.defect_indices[-self.n_last_lines:, :]

    def __calc_overlap(self, s1:int,e1:int , s2:int, e2:int):
        distance = min(e1, e2) - max(s1, s2)

        return distance
    

    def __add__(self, other:Defect):
        if other is None:
            return self
        res_defect = Defect(None,None,None,None)

        res_defect.start_line_idx = min(self.start_line_idx, other.start_line_idx)
        res_defect.end_line_idx = max(self.end_line_idx, other.end_line_idx)
        res_defect.n_last_lines = max(self.n_last_lines, other.n_last_lines)

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
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


class Defect:
    def __init__(
            self,
            start_anomaly_idx: int,
            end_anomaly_idx: int,
            start_line_idx: int,
            depthes: np.ndarray,
            n_last_defects: int = 3
        ):
        self.widthInfo = numberStatics()
        self.depthInfo = numberStatics()

        self.n_last_defects = n_last_defects
        self.defect_indices = np.array(([[start_anomaly_idx, end_anomaly_idx]]))
        
        self.start_line_idx = start_line_idx
        self.end_line_idx = self.start_line_idx

        self.defect_width_boundries = (start_anomaly_idx, end_anomaly_idx)

        self.__append_width_info(start_anomaly_idx, end_anomaly_idx)
        self.__append_depth_info(depthes)

    def append_line(self, start_anomaly_idx, end_anomaly_idx, depthes, line_idx):
        self.__append_width_info(start_anomaly_idx, end_anomaly_idx)
        self.__append_depth_info(depthes)
        self.__append_idx(start_anomaly_idx, end_anomaly_idx)
        self.end_line_idx = line_idx
        self.defect_width_boundries = (
            min(self.defect_width_boundries[0], start_anomaly_idx),
            max(self.defect_width_boundries[1], end_anomaly_idx)
        )

    def is_complete(self, line_idx:int, min_idx_gap):
        if line_idx - self.end_line_idx >= min_idx_gap:
            return True
        return False
    
    def is_defect(self, min_length: int):
        if (self.end_line_idx - self.start_line_idx) > min_length:
            return True
        else:
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
        
    def get_bounding_box(self, line_idx):
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
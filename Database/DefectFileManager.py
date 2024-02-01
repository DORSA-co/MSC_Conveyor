import json
import os

import numpy as np
from persiantools.jdatetime import JalaliDateTime

from Detection.Defect import Defect, numberStatics

class DefectFileManager:
    def __init__(self, main_path):
        self.main_path = main_path

    def defect_to_json(self, defect:Defect):
        json_dict = {}
        json_dict['id'] = defect.id
        json_dict['width_info'] = self.number_statics_to_json(defect.widthInfo)
        json_dict['depth_info'] = self.number_statics_to_json(defect.widthInfo)

        json_dict['date'] = defect.jdatetime.strftime('%Y/%m/%d')
        json_dict['time'] = defect.jdatetime.strftime('%H:%M:%S')

        json_dict['n_last_lines'] = defect.n_last_lines

        json_dict['defect_indices'] = defect.defect_indices.tolist()

        json_dict['start_line_idx'] = defect.start_line_idx
        json_dict['end_line_idx'] = defect.end_line_idx

        json_dict['defect_width_boundries'] = (int(defect.defect_width_boundries[0]), int(defect.defect_width_boundries[1]))

        return json_dict

    def number_statics_to_json(self, number_static:numberStatics):
        json_dict = {}
        json_dict['mean'] = float(number_static.mean)
        json_dict['min'] = float(number_static.min)
        json_dict['max'] = float(number_static.max)
        json_dict['count'] = int(number_static.count)

        return json_dict
    
    def json_to_number_statics(self,  json_dict:dict):
        number_static = numberStatics()
        number_static.max = json_dict['max']
        number_static.min = json_dict['min']
        number_static.mean = json_dict['mean']
        number_static.count = json_dict['count']

    def json_to_defect(self, json_dict)-> Defect:
        defect = Defect()
        
        defect.id = int(json_dict['id'])
        defect.widthInfo = self.json_to_number_statics(json_dict['width_info'])
        defect.widthInfo = self.json_to_number_statics(json_dict['depth_info'])

        defect.jdatetime = JalaliDateTime.strptime(json_dict['date']+json_dict['time'], '%Y/%m/%d%H:%M:%S')

        defect.n_last_lines = json_dict['n_last_lines']

        defect.defect_indices = np.array(json_dict['defect_indices'], dtype=np.int32)

        defect.start_line_idx = np.array(json_dict['start_line_idx'], dtype=np.int32)
        defect.end_line_idx = np.array(json_dict['end_line_idx'], dtype=np.int32)

        defect.defect_width_boundries = json_dict['defect_width_boundries']

        return defect

    def path_builder(self, defect_id):
        return os.path.join(self.main_path, str(defect_id)+'.json')

    def save(self, defect: Defect):
        json_dict = self.defect_to_json(defect)
        path = self.path_builder(defect.id)

        with open(path, 'w') as f:
            json.dump(json_dict, f)

    def remove(self, defect_id: str):
        path = self.path_builder(defect_id)
        if os.path.exists(path):
            os.remove(path)

        else:
            print('DefectFileManager: Path does not exist')

    def load_json(self, defect_id) -> dict:
        path = self.path_builder(defect_id)

        with open(path, 'r') as f:
            defect_json = json.load(f)

        return defect_json

    def load_defect(self, defect_id) -> Defect:
        defect_json = self.load_json(defect_id)
        defect = self.json_to_defect(defect_json)
        return defect

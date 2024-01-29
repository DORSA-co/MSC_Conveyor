import json
import os

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

    def json_to_defect():
        pass

    def path_builder(self, defect_id):
        return os.path.join(self.main_path, str(defect_id)+'.json')

    def save(self, defect: Defect):
        json_dict = self.defect_to_json(defect)
        path = self.path_builder(defect.id)

        with open(path, 'w') as f:
            json.dump(json_dict, f)

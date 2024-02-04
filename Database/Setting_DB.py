from Database.databaseManager import databaseManager
from Detection.AnomalyDetection import ANOMALY_ALGORITHMS


class parentSettingDB:
    TABLE_NAME = ""
    TABLE_COLS = []
    TABLE_DEFAULT_DATAS = []

    def __init__(self,db_manager: databaseManager):
        self.db_manager = db_manager

    
    def __create_table__(self,):
        if not self.db_manager.table_exits(self.TABLE_NAME):
            self.db_manager.create_table(self.TABLE_NAME)
            
            for col in self.TABLE_COLS:
                self.db_manager.add_column( self.TABLE_NAME, **col)
                
                self.restor_default()

    def restor_default(self):
        for default_data in self.TABLE_DEFAULT_DATAS:
            self.save(default_data)
        
    def save(self,record:dict):
        pass
        # assert len(record) == len(self.TABLE_COLS), 'data count arent equal to table columns'

        #Re Implement this method




class settingDB:
    def __init__(self, db_manager:databaseManager) -> None:
        self.camera_setting_db = cameraSettingDB(db_manager=db_manager)
        self.algorithm_setting_db = algorithmSettingDB(db_manager=db_manager)




class cameraSettingDB(parentSettingDB):
    TABLE_NAME = "camera_setting"
    TABLE_COLS = [
        {"col_name": "name",  "type": "VARCHAR(255)", "len": 50},
        {"col_name": "serial_number",  "type": "VARCHAR(255)", "len": 50},
        {"col_name": "width", "type": "INT"},
        {"col_name": "height", "type": "INT"},
        {"col_name": "exposure", "type": "INT"},
        {"col_name": "gain", "type": "INT"},
        {"col_name": "offset_x", "type": "INT"},
        {"col_name": "offset_y", "type": "INT"},
        
        
    ]
    
    
    TABLE_DEFAULT_DATAS= [ {
                            'name': 'main',
                            'serial_number': '',
                            'gain': 0,           
                            'exposure': 7000,       
                            'width':  640,          
                            'height': 480,         
                            'offset_x': 16,  
                            'offset_y': 16,
                        }   
                    ]
    
    PRIMERY_KEY_COL_NAME = 'name'

    def __init__(self, db_manager: databaseManager):
        super(cameraSettingDB, self).__init__(db_manager)
        
        self.db_manager = db_manager
        self.__create_table__()



    def is_exist(self, application):
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, application)
        if len(founded_records)>0:
            return True
        return False



    def save(self, data):
        super().save(data)
        if self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.update_record_dict(self.TABLE_NAME,data, self.PRIMERY_KEY_COL_NAME, data[self.PRIMERY_KEY_COL_NAME])
        else:
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
    

    def load(self, camera_application):

        record =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, camera_application)
        if len(record)>0:
            return record[0]
        return {}
    
    def get_camera_devices(self,) -> dict:
        records =  self.db_manager.get_all_content(self.TABLE_NAME)
        res = []
        for record in records:
            res.append(
                {'name': record['name'],
                  'serial_number': record['serial_number'] }
            )


        return res
    







class algorithmSettingDB(parentSettingDB):
    TABLE_NAME = "algorithm_setting"
    TABLE_COLS = [
        {"col_name": "background_thresh", "type": "INT"},
        {"col_name": "conv_window_size",  "type": "INT"},
        {"col_name": "diff_thresh",       "type": "INT"},
        {"col_name": "anomaly_algorithm", "type": "VARCHAR(255)", "len": 100},
        {"col_name": "defect_min_width",  "type": "INT"},
        {"col_name": "tracker_min_frame_gap",  "type": "INT"},
        {"col_name": "defect_min_length",  "type": "INT"},
        {"col_name": "image_width",  "type": "INT"},
    ]
    
    
    TABLE_DEFAULT_DATAS= [ {
                            'background_thresh': 25,
                            'conv_window_size': 10,
                            'diff_thresh': 2,
                            'anomaly_algorithm': ANOMALY_ALGORITHMS.LINE_FIT,
                            'defect_min_width': 3,
                            'tracker_min_frame_gap': 80,
                            'defect_min_length': 5,
                            'image_width': 1000,
                        }   
                    ]
    
    PRIMERY_KEY_COL_NAME = 'id'

    def __init__(self, db_manager):
        super().__init__(db_manager)
        self.__create_table__()
        
        
    def is_exist(self, id):
        founded_records = self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(founded_records)>0:
            return True
        return False


    def save(self, data):
        data['id'] = 1
        super().save(data)
        if self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.update_record_dict(self.TABLE_NAME,data, self.PRIMERY_KEY_COL_NAME, data[self.PRIMERY_KEY_COL_NAME])
        else:
            self.db_manager.add_record_dict(self.TABLE_NAME, data)
    

    def load(self):
        id = 1
        record:dict =  self.db_manager.search( self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, id)
        if len(record)>0:
            record = record[0]
            record.pop('id')
            return record
        return {}
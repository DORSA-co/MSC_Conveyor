from Database.databaseManager import databaseManager
## DATE ##
from persiantools import jdatetime
# import datetime

class Defect_DB:
    TABLE_NAME = "Defect_Table"
    TABLE_COLS = [
        {"col_name": "defect_id", "type": "bigint"},

        {"col_name": "date", "type": "VARCHAR(255)", "len": 50},
        {"col_name": "time", "type": "VARCHAR(255)", "len": 50},

        {"col_name": "x", "type": "int"},
        {"col_name": "y", "type": "int"},

        {"col_name": "min_width", "type": "float(10,3)"},
        {"col_name": "mean_width", "type": "float(10,3)"},
        {"col_name": "max_width", "type": "float(10,3)"},

        {"col_name": "min_depth", "type": "float(10,3)"},
        {"col_name": "mean_depth", "type": "float(10,3)"},
        {"col_name": "max_depth", "type": "float(10,3)"},

        {"col_name": "length", "type": "float(10,3)"},

        {"col_name": "main_path", "type": "Text"},
    ]

    PRIMERY_KEY_COL_NAME = 'defect_id'

    def __init__(self, db_manager:databaseManager):
        self.db_manager = db_manager
        self.__create_table__()
        #self.TABLE_NAME="reports76"

    def __create_table__(
        self,
    ):
        self.db_manager.create_table(self.TABLE_NAME)
        for col in self.TABLE_COLS:
            self.db_manager.add_column(self.TABLE_NAME, **col)


    def is_exist(self, defect_id):
        founded_records = self.db_manager.search(
            self.TABLE_NAME, self.PRIMERY_KEY_COL_NAME, defect_id
        )
        if len(founded_records) > 0:
            return True
        return False

    def save(self, data):
        data['date'] = data['date'].strftime('%Y/%m/%d')
        data['time'] = data['time'].strftime('%H:%M:%S')
        if self.is_exist(data[self.PRIMERY_KEY_COL_NAME]):
            self.db_manager.update_record_dict(
                self.TABLE_NAME,
                data,
                self.PRIMERY_KEY_COL_NAME,
                data[self.PRIMERY_KEY_COL_NAME],
            )
        else:
            self.db_manager.add_record_dict(self.TABLE_NAME, data)


    def load(self):
         records=self.db_manager.get_all_content(self.TABLE_NAME, reverse_order=True)
         for record in records:
            ## DATE ##
            record['date'] = jdatetime.JalaliDateTime.strptime(record['date'], '%Y/%m/%d')
            record['time'] = jdatetime.JalaliDateTime.strptime(record['time'], '%H:%M:%S')

         return records
      
    def remove_record(self,column_name, Select_ID):

        records = self.db_manager.remove_record(self.TABLE_NAME, column_name, str(Select_ID))
        return records
    
    
    def  search(self,column_name, Select_ID):
         records = self.db_manager.search(self.TABLE_NAME, column_name, Select_ID)
         return records
    
    def search_Total(self):
         records = self.db_manager.search_Total(self.TABLE_NAME)
         return records
    

    def search_interval(self,column_name,min_of_interval,max_of_interval):
         records = self.db_manager.search_interval(
                    self.TABLE_NAME,
                   column_name,
                    min_of_interval,
                    max_of_interval,
                )
         return  records
    
    def add_record(self,value):

     self.db_manager.add_record(
                        self.TABLE_NAME,
                        value
                    )
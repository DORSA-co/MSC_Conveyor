
from Database.databaseManager import databaseManager
from Database.Report_DB import Report_DB
from Database.Setting_DB import settingDB

class mainDatabase:
    username = "root"
    #password = "dorsa-co"
    password = ""
    HOST = "localhost"
    DATABASE_NAME = "test_database"

    def __init__(
        self,
    ):
        self.dbManager = None
        self.__connect__()

        self.Report_DB = Report_DB(self.dbManager)
        self.Setting_DB = settingDB(self.dbManager)
       

    def __connect__(
        self,
    ):
        self.dbManager = databaseManager(
            self.username, self.password, self.HOST, self.DATABASE_NAME, log_level=1
        )




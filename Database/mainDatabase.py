
from Database.databaseManager import databaseManager
from Database.Setting_DB import settingDB
from Database.users_DB import usersDB
from Database.Defects_DB import Defect_DB

class mainDatabase:
    username = "root"
    #password = "dorsa-co"
    password = "Dorsa-1400"
    password = ""
    HOST = "localhost"
    DATABASE_NAME = "dci_database"

    def __init__(
        self,
    ):
        self.dbManager = None
        self.__connect__()

        self.Setting_DB = settingDB(self.dbManager)
        self.Users_DB = usersDB(self.dbManager)
        self.Defects_DB = Defect_DB(self.dbManager)

    def __connect__(
        self,
    ):
        self.dbManager = databaseManager(
            self.username, self.password, self.HOST, self.DATABASE_NAME, log_level=1
        )




import sys
import os
sys.path.append('UIFiles\\assets')

os.system('pyside6-uic UIFiles\\main_UI.ui -o UIFiles\\main_UI.py')
os.system('pyside6-rcc UIFiles\\assets\\assets.qrc -o UIFiles\\assets\\assets_rc.py')

from PySide6.QtWidgets   import QApplication

from main_API import main_API
from main_UI import mainUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_ui = mainUI()
    API = main_API(main_ui)
    main_ui.show()
    app.exec()
import sys
import os
sys.path.append(os.path.join('UIFiles', 'assets'))
sys.path.append('uiUtils')

os.system('pyside6-rcc {} -o {}'.format(os.path.join('UIFiles', 'assets', 'assets.qrc'), os.path.join('UIFiles', 'assets', 'assets_rc.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'main_UI.ui'), os.path.join('UIFiles', 'main_UI.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'defect_notification.ui'), os.path.join('UIFiles', 'defect_notification.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'edit_user.ui'), os.path.join('UIFiles', 'edit_user.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'login_UI.ui'), os.path.join('UIFiles', 'login_UI.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'popup_slider.ui'), os.path.join('UIFiles', 'popup_slider.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'image_viewer.ui'), os.path.join('UIFiles', 'image_viewer.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'belt_tile.ui'), os.path.join('UIFiles', 'belt_tile.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'progress_dialog.ui'), os.path.join('UIFiles', 'progress_dialog.py')))

from PySide6.QtWidgets import QApplication

from main_API import main_API
from main_UI import mainUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    main_ui = mainUI()
    API = main_API(main_ui)
    main_ui.show()
    app.exec()
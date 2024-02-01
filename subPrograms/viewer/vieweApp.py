import sys
import os

sys.path.insert(1, os.getcwd())
sys.path.append(os.path.join('UIFiles', 'assets'))
sys.path.append('uiUtils')

os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'image_viewer.ui'), os.path.join('UIFiles', 'image_viewer.py')))
os.system('pyside6-uic {} -o {}'.format(os.path.join('UIFiles', 'belt_tile.ui'), os.path.join('UIFiles', 'belt_tile.py')))

from PySide6.QtWidgets import QApplication

from viewerUI import viewerUI
from viewerAPI import viewerAPI

if __name__ == "__main__":
    app = QApplication(sys.argv)

    sys.argv.append('199918347')
    
    if len(sys.argv) >= 2:
        viewer_ui = viewerUI()
        API = viewerAPI(viewer_ui, sys.argv[1])
        viewer_ui.show()
        app.exec()


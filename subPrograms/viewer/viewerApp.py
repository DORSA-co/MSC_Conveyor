import sys
import os
import argparse

parser=argparse.ArgumentParser(description="viewer argument parser")
parser.add_argument('-id', '--defect_id', type=int)
parser.add_argument('--path', type=str, default=os.getcwd())
args=parser.parse_args()
print('Start')
#args.defect_id = 2354061969344

sys.path.append(args.path)
sys.path.append(os.path.join('UIFiles', 'assets'))
sys.path.append('uiUtils')

from PySide6.QtWidgets import QApplication

from subPrograms.viewer.viewerUI import viewerUI
from subPrograms.viewer.viewerAPI import viewerAPI

if __name__ == "__main__":
    app = QApplication(sys.argv)

    #sys.argv.append('199918347')
    #sys.
    
    # if args.defect_id:
    viewer_ui = viewerUI()
    #API = viewerAPI(viewer_ui, sys.argv[1])
    API = viewerAPI(viewer_ui, args.defect_id)
    viewer_ui.show()
    app.exec()


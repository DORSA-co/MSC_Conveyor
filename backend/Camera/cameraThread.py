import os
import time

import cv2
import numpy as np
from PySide6.QtCore import QThread
from PySide6.QtCore import Signal, QMutex, QObject

from backend.Camera.dorsaPylon import Camera, Collector
from Constants import Constant

def DemoImageLoader(path):
        files = sorted(os.listdir(path))
        files.reverse()
        total_count = len(files)
        start_idx = 70
        while True:
            total_range = list(range(start_idx, total_count)) + list(range(0,start_idx))
            for i in total_range:
                fpath = os.path.join(path, files[i])
                yield cv2.imread(fpath,0)




class cameraWorker(QObject):
    success_grab_signal = Signal(np.ndarray)
    grabb_image_error = Signal()
    finished = Signal()

    


    def __init__(self, camera:Camera, timeout = 2000):
        super().__init__()
        self.camera = camera
        self.grabbing = True
        self.new_camera = None
        self.timeout = timeout

        if camera.Infos.is_Simulation():
            self.simulation = True
            self.demoImageLoader = DemoImageLoader(Constant.DemoImage.DIR)
        else:
            self.simulation = False
            self.demoImageLoader = None

    def change_camera(self, new_camera):
        self.new_camera = new_camera

    
    def grabber(self,):
        # t = 0
        self.time = time.time()
        while self.grabbing:

            try:
                if self.new_camera:
                    self.camera = self.new_camera
                    self.new_camera = None

                if (time.time() - self.time) * 1000 > self.timeout:
                    self.grabb_image_error.emit()
                    self.time = time.time()

                if self.camera.Status.is_grabbing():
                    ret, img = self.camera.getPictures(img_when_error=None)
                    if ret:
                        if not self.simulation:
                            self.success_grab_signal.emit(img)
                        else:
                            img = next(self.demoImageLoader)
                            self.success_grab_signal.emit(img)
                        self.time = time.time()
                
                else:
                    self.time = time.time()
                
                
                

            except Exception as e:
                print('camera Error happend in thread while !', repr(e))
            
            time.sleep(0.01)

        print('end of Camra Thread While')
        self.finished.emit()





class DeviceCheckerWorker(QObject):
    finished = Signal()

    serials_ready = Signal()
    def __init__(self, collector: Collector) -> None:
        self.collector = collector
        super().__init__()

    def serial_number_finder(self):
        for i in range(1):
            try:
                self.available_serials = self.collector.get_all_serials()
                self.serials_ready.emit()
            except:
                self.available_serials = []

    def get_available_serials(self):
        return self.available_serials

import sys
import os
import threading

import numpy as np
import cv2
import time

if __name__ == "__main__":
    sys.path.append(os.getcwd())

from PySide6.QtCore import QObject, Signal
from memory_profiler import profile


from Detection.laserScanner import laserScanner
from Detection.AnomalyDetection import AnomalyDetectionHandeler, ANOMALY_ALGORITHMS
from Detection.DefectExtractor import DefectExtractor
from Detection.ImageCreator import ImageCreator
from Detection.Encoder import Encoder
from Detection.DefectTracker import DefectTracker
from Detection.Defect import Defect
from Constants.Constant import DefectConstants

PRINT_FLAG = True
TIME_MONITORING_FLAG = False

class beltInspection(QObject):
    processing_finished = Signal()
    new_defect = Signal(Defect)
    update_defect = Signal(Defect)

    def __init__(self, kwargs:dict) -> None:
        super(beltInspection, self).__init__()
        self.kwargs = kwargs
        self.LaserScanner = laserScanner()
        self.AnomalyDetection = AnomalyDetectionHandeler()
        self.DefectExtractor = DefectExtractor()
        self.Encoder = Encoder()
        self.DefectTracker = DefectTracker()
        self.ImageCreator = ImageCreator((640, self.kwargs['image_width']),
                                         max_y_errors=DefectConstants.MAX_Y_ERRORS )
        

        self.res_image = self.ImageCreator.image.copy()
        self.line_idx = 0
        self.image = self.ImageCreator.image.copy()

        self.DefectTracker.set_new_defect_event(self.new_defect_happend_event)
        self.DefectTracker.set_update_defect_event(self.defect_update_event)
        self.Encoder.set_finish_event(self.round_finish_event)
        self.ImageCreator.set_cycle_image_event(self.cycle_image_event)


    
    def change_settings(self, kwargs:dict):
        self.kwargs = kwargs

    #@profile
    def feed(self, image:np.ndarray):
        
        #ONLY FOR TEST
        image = np.hstack((image,)*8)
        
        #ONLY FOR TEST


        if not self.ImageCreator.check_image_size(image.shape):
            self.ImageCreator = ImageCreator((image.shape[1], self.kwargs['image_width']),
                                         max_y_errors=DefectConstants.MAX_Y_ERRORS )
            self.ImageCreator.set_cycle_image_event(self.cycle_image_event)
        
        
        t = time.time()
        #t_total = time.time()
        

        # SHOULD BE CHANGED
        self.Encoder.counter()
        line_idx = self.Encoder.get_line_idx()
        #print(line_idx)
        # return
        # SHOULD BE CHANGED
        t = time.time()
        
        self.laser_pts = self.LaserScanner.laserExtraction(image,
                                     thresh=self.kwargs['background_thresh'],
                                      win_size=self.kwargs['conv_window_size'] )

        if TIME_MONITORING_FLAG: 
            print('laser extraction: ', time.time() - t)
        
        
        # detect start and stop points
        t = time.time()
        self.anomaly_pts = self.AnomalyDetection.feed(self.laser_pts, 
                                   diff_thresh=self.kwargs['diff_thresh'],
                                   algorithm=self.kwargs['anomaly_algorithm']
        )

        
        
        
        if TIME_MONITORING_FLAG:
            print('anomaly detection: ', time.time() - t)
        
        t = time.time()
        self.defect_indices = self.DefectExtractor.feed(self.anomaly_pts, min_width=self.kwargs['defect_min_width'])
        if TIME_MONITORING_FLAG:
            print('defect extractor: ', time.time() - t)


        t = time.time()
        self.DefectTracker.feed(self.defect_indices, 
                                self.anomaly_pts[:, 1], 
                                line_idx,
                                self.Encoder.get_end_line_idx())
        if TIME_MONITORING_FLAG:
            print('defect tracker: ', time.time() - t)

        

        t = time.time()
        self.DefectTracker.check_defects_completion(self.kwargs['tracker_min_frame_gap'], 
                                                    self.kwargs['defect_min_length'], 
                                                    line_idx,
                                                    )
        if TIME_MONITORING_FLAG:
            print('check completion: ', time.time() - t)
        
        t = time.time()   
        image = self.ImageCreator.feed(self.anomaly_pts, 'color_gradient', line_idx)
        if TIME_MONITORING_FLAG:
            print('image creator: ', time.time() - t)

        t = time.time()
        #--------------------------------------
        self.DefectTracker.check_defect_passed(line_idx=line_idx,
                                               img_width=image.shape[1],
                                               )
        if TIME_MONITORING_FLAG:
            print('check defect pass ', time.time() - t)

        self.line_idx = line_idx
        self.image = image
        
                
                
        

        # cv2.putText(self.res_image, 
        #             text=str(self.Encoder.line_idx),
        #             org=(20,20),
        #             fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL,
        #             fontScale=1,
        #             color=(0,0,0),
        #             thickness=2)

        # cv2.imshow('', res_image)
        #---------------------------------------------------
        self.processing_finished.emit()


    def get_result_image(self) -> np.ndarray:
        t = time.time()
        # image = image.copy()
        self.res_image = self.DefectTracker.draw(self.kwargs['defect_min_length'],
                                                self.image.copy(), 
                                                self.line_idx,
                                                )
        if TIME_MONITORING_FLAG:
            print('last draw: ', time.time() - t)
        return self.res_image
    
    def find_defect(self, _id)-> Defect:
        return self.DefectTracker.completed_defects.get_by_id(_id)
    
    def round_finish_event(self, finish_idx):
        if PRINT_FLAG:
            print('End Belt',finish_idx)
        self.ImageCreator.reset_image_index(finish_idx)

    def cycle_image_event(self,image_index, image_start_line_idx):
        if PRINT_FLAG:
            print('save depth image:',image_index, image_start_line_idx)
        save_thread = threading.Thread(target=self.ImageCreator.save_depth_image,
                                       args=(image_index, image_start_line_idx))
        save_thread.start()

    def new_defect_happend_event(self, defect:Defect):
        """this function call from DefectTracker when new defect occur
        """
        pass
        self.new_defect.emit(defect)
        # self.external_new_defect_event_func(defect)
    
    def defect_update_event(self, defect:Defect):
        pass
        self.update_defect.emit(defect)
        #self.external_defect_update_event_func(defect)






if __name__ == "__main__":

    import threading
    import psutil
    
    from backend.Camera.cameraThread import DemoImageLoaderRAM
    from Constants.Constant import DemoImage
    from Database import mainDatabase
    from PySide6.QtWidgets import QMainWindow, QApplication

    


    #----------------------------------------------------------
    # import psutil,os
    
    processes = []
    for process in psutil.process_iter(): 
        processes.append(process)

    processes.sort(key= lambda x:x.name())
    for process in processes:
        if 'task' in process.name().lower():
            print(process.kill())

    # os.system('taskmgr')
    #----------------------------------------------------------

    

    class Test(QMainWindow):
        def __init__(self, ) -> None:
            super(Test, self).__init__()
            self.is_processing = False

            self.demoImageLoader = DemoImageLoaderRAM(DemoImage.DIR)

            self.db = mainDatabase.mainDatabase()
            kwargs = self.db.Setting_DB.algorithm_setting_db.load()
            self.bi = beltInspection(kwargs)
            self.bi.processing_finished.connect(lambda: print('استاد اوگوی') )

        @staticmethod
        def print_memory_usage():
            process = psutil.Process(os.getpid())
            memory_usage = process.memory_info().rss # in bytes 
            print(f"Memory Usage: {memory_usage / 1024**2:.2f} MB")

        def run(self,):
            for img in  self.demoImageLoader:
                if not self.is_processing:
                    t= time.time()
                    self.is_processing = False
                    th = threading.Thread(target=self.bi.feed, args=(img,))
                    th.start()
                    th.join()
                    # self.test_thread(img)
                    print(time.time() - t)
                    self.print_memory_usage()

        def processing_finished_event(self,):
            print('abads')
            global is_processing
            is_processing = False

        def test_thread(self, img):
            self.img = img
            print('test thread func')
    

    app = QApplication(sys.argv)
    
    test = Test()
    test.run()
    app.exec()
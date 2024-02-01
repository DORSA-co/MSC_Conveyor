import os
import json

import numpy as np
import cv2

from Detection import heatMap
from Constants.Constant import SavePathes

class ImageCreator:
    def __init__(self, image_size: tuple, max_y_errors: int) -> None:
        self.image_size = image_size
        self.image = np.zeros(image_size + (3,), dtype=np.uint8)
        self.depth_image = np.zeros(image_size, dtype=np.float32)
        self.gradiants = {}
        self.max_y_errors = max_y_errors

        self.external_cycle_image_event_func = None
        self.cycle_idx = 0
        self.total_idx = image_size[1]
        self.image_index = 0

        self.image_start_line_idx = 0

        self.create_gradient('color_gradient', heatMap.GRADIENT1)
        
        self.create_gradient('gray_gradient', ( ((220, 220, 220), 0),
                                                ((150, 150, 150), 0.19), 
                                                ((0, 0, 0), 0.2), 
                                                ((100, 100, 100), 0.45), 
                                                ((100, 100, 100), 0.5), 
                                                ((100, 100, 100), 0.55),
                                                ((0, 0, 0), 0.8),
                                                ((150, 150, 150), 0.81),
                                                ((220, 220, 220), 1),
                                                ))
        
        self.create_metadata()
    
    def set_cycle_image_event(self, func):
        self.external_cycle_image_event_func = func

    def create_gradient(self, name: str, colors: list[tuple]) -> None:
        cg = heatMap.colorGradient()
        for color in colors:
            cg.add_color(color[0], color[1])
        
        self.gradiants[name] = cg.generate_gradiant(self.max_y_errors*2)

    def feed(self, error_ys: np.ndarray, gradient_name: str, step: int, line_idx: int):
        self.image[:, step:] = self.image[:,: - (step) ]
        self.depth_image[:, step:] = self.depth_image[:,: - (step) ]

        #---------------------------------------------------------------------
        error_ys_norm = error_ys + self.max_y_errors
        error_ys_norm = np.clip(error_ys_norm, 0, 2*self.max_y_errors - 1)
        new_line = self.gradiants[gradient_name][error_ys_norm[:,1]]
        new_line = np.expand_dims(new_line, axis=1)
        self.image[:,:step] = np.tile(new_line, (1,step,1))
        #---------------------------------------------------------------------
        new_line_depth = np.expand_dims(error_ys[:,1], axis=1)
        self.depth_image[:,:step] = np.tile(new_line_depth, (1,step))
        #---------------------------------------------------------------------
        # print('^'*10, line_idx)
        if self.cycle_idx == 0:
            self.image_start_line_idx = line_idx
            # print('#'*10, line_idx)

        if line_idx != 0:
            self.cycle_idx += step

        if self.cycle_idx >= self.total_idx:
            self.image_index +=1
            self.image_start_line_idx = line_idx - self.cycle_idx
            # print('&'*10, self.cycle_idx, line_idx, self.image_start_line_idx)
            self.cycle_idx = self.cycle_idx - self.total_idx
            self.external_cycle_image_event_func()

        return self.image

    def reset_image_index(self):
        self.image_index += 1
        # self.external_cycle_image_event_func()
        self.image_index = 0
        self.cycle_idx = 0

    def create_metadata(self):
        path = os.path.join(SavePathes.IMAGE_SAVE_PATH, SavePathes.METADATA_JASON_FILE)
        with open(path, 'w') as fp:
            json.dump({}, fp)

    def update_metadata(self, image_index):
        path = os.path.join(SavePathes.IMAGE_SAVE_PATH, SavePathes.METADATA_JASON_FILE)
        with open(path, 'r') as fp:
            metadata = json.load(fp)

        metadata[str(image_index)] = (self.image_start_line_idx, self.image_start_line_idx+self.total_idx)

        with open(path, 'w') as fp:
            json.dump(metadata, fp)

    def save_depth_image(self):
        imag_index = self.image_index
        path = os.path.join(SavePathes.IMAGE_SAVE_PATH, str(imag_index) + '.npy')
        with open(path, 'wb') as f:
            np.save(f, self.depth_image)

        self.update_metadata(imag_index)
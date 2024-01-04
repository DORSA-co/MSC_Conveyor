import numpy as np
import cv2

from Detection import heatMap


class ImageCreator:
    def __init__(self, image_size: tuple, step: int, max_y_errors: int) -> None:
        self.image_size = image_size
        self.step = step
        self.image = np.zeros(image_size + (3,), dtype=np.uint8)
        self.gradiants = {}
        self.max_y_errors = max_y_errors

        self.create_gradient('color_gradient', (((19, 47, 186), 0), 
                                                ((30, 115, 227), 0.15), 
                                                ((9, 162, 222), 0.3), 
                                                ((150, 150, 150), 0.45), 
                                                ((150, 150, 150), 0.5), 
                                                ((150, 150, 150), 0.55),
                                                ((9, 162, 222), 0.7),
                                                ((30, 115, 227), 0.85),
                                                ((19, 47, 186), 1),
                                                ))
        
        self.create_gradient('gray_gradient', ( ((220, 220, 220), 0),
                                                ((0, 0, 0), 0.25), 
                                                ((100, 100, 100), 0.45), 
                                                ((100, 100, 100), 0.5), 
                                                ((100, 100, 100), 0.55),
                                                ((0, 0, 0), 0.75),
                                                ((220, 220, 220), 1),
                                                ))

    def create_gradient(self, name: str, colors: list[tuple]) -> None:
        cg = heatMap.colorGradient()
        for color in colors:
            cg.add_color(color[0], color[1])
        
        self.gradiants[name] = cg.generate_gradiant(self.max_y_errors*2)

    def feed(self, error_ys: np.ndarray, gradient_name: str):
        self.image[:, self.step:] = self.image[:,: - (self.step) ]

        error_ys = error_ys + self.max_y_errors
        new_line = self.gradiants[gradient_name][error_ys[:,1]]
        new_line = np.expand_dims(new_line, axis=1)
        self.image[:,:self.step] = np.tile(new_line, (1,2,1))
        cv2.imshow('', self.image)

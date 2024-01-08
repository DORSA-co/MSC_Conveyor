import numpy as np
import cv2

from Detection import heatMap


class ImageCreator:
    def __init__(self, image_size: tuple, max_y_errors: int) -> None:
        self.image_size = image_size
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
                                                ((150, 150, 150), 0.19), 
                                                ((0, 0, 0), 0.2), 
                                                ((100, 100, 100), 0.45), 
                                                ((100, 100, 100), 0.5), 
                                                ((100, 100, 100), 0.55),
                                                ((0, 0, 0), 0.8),
                                                ((150, 150, 150), 0.81),
                                                ((220, 220, 220), 1),
                                                ))

    def create_gradient(self, name: str, colors: list[tuple]) -> None:
        cg = heatMap.colorGradient()
        for color in colors:
            cg.add_color(color[0], color[1])
        
        self.gradiants[name] = cg.generate_gradiant(self.max_y_errors*2)

    def feed(self, error_ys: np.ndarray, gradient_name: str, step: int):
        self.image[:, step:] = self.image[:,: - (step) ]

        error_ys = error_ys + self.max_y_errors
        error_ys = np.clip(error_ys, 0, 2*self.max_y_errors - 1)
        new_line = self.gradiants[gradient_name][error_ys[:,1]]
        new_line = np.expand_dims(new_line, axis=1)
        self.image[:,:step] = np.tile(new_line, (1,step,1))

        return self.image

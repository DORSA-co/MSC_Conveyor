import os
import json

import numpy as np
import cv2

from viewerUI import viewerUI
from Database.mainDatabase import mainDatabase
from Detection.Defect import Defect
from Database.DefectFileManager import DefectFileManager
from Constants.Constant import SavePathes
from Detection import heatMap
from Constants.Constant import DefectConstants

import view3D

class viewerAPI:
    def __init__(self, uiHandeler:viewerUI, defect_id: str) -> None:
        self.uiHandeler = uiHandeler

        self.db = mainDatabase()

        self.defect_id = defect_id

        self.max_y_errors = DefectConstants.MAX_Y_ERRORS
        
        self.gradiants = {}
        self.gradiants['color_gradient'] = self.create_gradient(heatMap.GRADIENT2)

        self.uiHandeler.tile_select_connector(self.select_tile_evet)
        self.defect_obj = self.get_defect()
        self.metadata = self.load_images_metadate()
        self.images_names = self.find_defect_images()
        self.setup_tiles(self.images_names)

        # self.current_image_idx = 0

        # self.render(self.current_image_idx)

        self.uiHandeler.button_connector('view_3d', self.view_3d)

        self.startup()
        self.uiHandeler.show_defect_info(self.defect_obj.get_info())

    def startup(self,):
        self.uiHandeler.startup()

    def get_defect(self) -> Defect:
        defect = self.db.Defects_DB.search('defect_id', self.defect_id)
        if not defect or len(defect) > 1:
            return
        
        defect = defect[0]
        defect_loader = DefectFileManager(defect['main_path'])
        defect_obj = defect_loader.load_defect(self.defect_id)
        
        return defect_obj

    def load_images_metadate(self) -> dict:
        metadata_path = os.path.join(SavePathes.IMAGE_SAVE_PATH, SavePathes.METADATA_JASON_FILE)
        with open(metadata_path, 'r') as fp:
            metadata = json.load(fp)

        return metadata
    
    def find_defect_images(self):
        images_names = []

        start_defect_idx = self.defect_obj.start_line_idx
        end_defect_idx = self.defect_obj.end_line_idx

        for image_idx in self.metadata:
            start_image_idx, end_image_idx = self.metadata[image_idx]
            if start_defect_idx <= end_image_idx and end_defect_idx >= start_image_idx:
                images_names.append(image_idx)

        return images_names
    
    def load_depth_image(self,  img_index : int):
        image_path = os.path.join(SavePathes.IMAGE_SAVE_PATH, str(img_index)+'.npy')
        with open(image_path, 'rb') as f:
            img = np.load(f)
            img = img.astype('int32')

        return img

    def depth_image_to_gradient_image(self, depth_image, gradient_name):
        image = np.zeros(depth_image.shape + (3,), dtype=np.uint8)
        normalize_depth = self.xyz[:, 2] + self.max_y_errors
        normalize_depth = np.clip( normalize_depth, 0, self.max_y_errors * 2 - 1)
        image[self.xyz[:, 1], self.xyz[:, 0]] = self.gradiants[gradient_name][normalize_depth]

        return image

    def create_gradient(self, colors: list[tuple]) -> None:
        cg = heatMap.colorGradient()
        for color in colors:
            cg.add_color(color[0], color[1])
        
        gradient = cg.generate_gradiant(self.max_y_errors*2)

        return gradient

    def create_xyz(self, depth_image):
        xyz = view3D.depthImage2xyz(depth_image)
        xyz = xyz.astype('int32')

        return xyz

    def draw_bounding_box(self, image: np.ndarray, color: tuple = (33, 33, 133)):
        line_idx = self.get_image_idx_boundry_idx(self.current_image_idx)[1]
        pt1, pt2 = self.defect_obj.get_bounding_box(line_idx)
        
        image = cv2.rectangle(image, pt1, pt2, color=color, thickness=2)
        return image
    
    def render(self, image_idx):
        self.depth_image = self.load_depth_image(self.images_names[image_idx])
        self.xyz = self.create_xyz(self.depth_image)
        self.gradient_image = self.depth_image_to_gradient_image(self.depth_image, 'color_gradient')
        self.gradient_image = self.draw_bounding_box(self.gradient_image)
        self.uiHandeler.set_image(self.gradient_image)

    def get_image_idx_boundry_idx(self, image_idx):
        return self.metadata[self.images_names[image_idx]]
    
    def view_3d(self):
        v3 = view3D.view3D()
        xyz = view3D.perfect_down_sample(self.xyz, 0.1)
        pcd = v3.numpy2pcd(xyz)
        mesh = v3.pcd2mesh(pcd)
        bbox = v3.generate_bbox((0, self.gradient_image.shape[1]), (0, self.gradient_image.shape[0]), (-20,20), border=10)
        mesh = v3.crop(mesh, bbox)
        
        v3.show_mesh(mesh)


    def setup_tiles(self, images_names):
        for i, img_name in enumerate(images_names):
            meterage = self.metadata[img_name]
            self.uiHandeler.add_tile(img_name, '#E0E4EC', meterage, select=(i==0))

    def select_tile_evet(self, _id:int):
        self.defect_obj = self.get_defect()
        self.current_image_idx = self.images_names.index(_id)
        print(self.current_image_idx )
        self.render(self.current_image_idx )
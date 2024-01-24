import sys
import numpy as np
import cv2

from PySide6.QtWidgets import QGraphicsView, QGraphicsScene, QApplication, QGraphicsPixmapItem
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap, QImage

class PhotoViewer(QGraphicsView):
    def __init__(self):
        super().__init__()

        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.pixmap_item = QGraphicsPixmapItem()
        self.scene.addItem(self.pixmap_item)

        self.setDragMode(QGraphicsView.ScrollHandDrag)
        self._zoom_factor = 1.15
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def set_numpy_image(self, np_image):
        height, width, channel = np_image.shape
        bytes_per_line = 3 * width
        q_img = QImage(np_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(q_img)
        self.pixmap_item.setPixmap(pixmap)
        self.setSceneRect(pixmap.rect())

    def wheelEvent(self, event):
        if event.angleDelta().y() > 0:
            self.zoom_in()
        else:
            self.zoom_out()

    def zoom_in(self):
        self.scale(self._zoom_factor, self._zoom_factor)

    def zoom_out(self):
        self.scale(1 / self._zoom_factor, 1 / self._zoom_factor)

# Example usage
if __name__ == '__main__':
    app = QApplication(sys.argv)
    viewer = PhotoViewer()

    # Create a sample NumPy image (replace with your actual NumPy image)
    np_image = cv2.imread('demo imgs/a.png')

    viewer.set_numpy_image(np_image)
    viewer.show()
    sys.exit(app.exec_())

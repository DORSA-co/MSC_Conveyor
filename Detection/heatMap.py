import numpy as np
import cv2


class gradientItem:
    def __init__(self, color, position) -> None:
        self.color = color
        self.position = position
        self.absolute_pos = -1

    def calc_absolute_pos(self, size):
        self.absolute_pos = int(self.position * size)


class colorGradient:
    def __init__(self) -> None:
        self.colors = []
        self.gradiant = None

    def add_color(self, color, position):
        self.colors.append(gradientItem(color, position))

    def reset(self):
        self.colors = []

    def generate_gradiant(self, size, smooth=True):


        self.colors.sort(key=lambda x: x.position)

        # if fisrt color start from mid:
        if self.colors[0].position > 0:
            self.colors.insert(0, gradientItem(self.colors[0].color, 0))

        if self.colors[-1].position < 1:
            self.colors.append(gradientItem(self.colors[-1].color, 1))

        self.gradiant = np.zeros((size, 3), dtype=np.uint8)

        for c_idx in range(len(self.colors) - 1):
            # ------------
            item1 = self.colors[c_idx]
            item2 = self.colors[c_idx + 1]
            item1.calc_absolute_pos(size)
            item2.calc_absolute_pos(size)
            # ------------
            for channle in range(3):
                ch = np.linspace(
                    item1.color[channle],
                    item2.color[channle],
                    item2.absolute_pos - item1.absolute_pos,
                    dtype=np.uint8,
                )
                self.gradiant[item1.absolute_pos : item2.absolute_pos, channle] = ch

        # ---------------- fill start

        if smooth:
            self.gradiant = np.reshape(self.gradiant, (1, -1, 3))
            self.gradiant = cv2.blur(self.gradiant, ksize=(int(size / 10), 1))
            self.gradiant = np.reshape(self.gradiant, (-1, 3))
        return self.gradiant

    def toImage(self, width):
        h, _ = self.gradiant.shape
        image = np.zeros((h, width, 3), dtype=np.uint8)
        for i in range(width):
            image[:, i] = self.gradiant
        return image




if __name__ == "__main__":
    cg = colorGradient()
    cg.add_color((19, 47, 186), 0)
    cg.add_color((30, 115, 227), 0.15)
    cg.add_color((9, 162, 222), 0.3)
    cg.add_color((150, 150, 150), 0.45)
    cg.add_color((150, 150, 150), 0.5)
    cg.add_color((150, 150, 150), 0.55)
    cg.add_color((9, 162, 222), 0.7)
    cg.add_color((30, 115, 227), 0.85)
    cg.add_color((19, 47, 186), 1)
    gradiant = cg.generate_gradiant(20)
    img = cg.toImage(200)

    cv2.imshow("grad", img)
    cv2.waitKey(0)

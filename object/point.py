from object.transform import transform_point
from PyQt5.QtCore import QPoint


class Point(QPoint, transform_point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.label = "Point ({},{})".format(x, y)

    def draw(self, painter):
        # Retorna uma tupla com (x, y)
        pointTransformed = self.transformViewport(self)
        painter.drawPoint(pointTransformed[0], pointTransformed[1])

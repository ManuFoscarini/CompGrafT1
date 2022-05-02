from object.transform import TransformPoint
from PyQt5.QtCore import QPoint


class Point(QPoint, TransformPoint):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y
        self.label = "Point ({},{})".format(x, y)

    def draw(self, painter):
        """Retorna uma tupla com (x, y)."""
        point_transformed = self.viewport_transformation(self)
        painter.drawPoint(point_transformed[0], point_transformed[1])
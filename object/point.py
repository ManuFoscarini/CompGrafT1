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

    def rotate(self, Point, angle):
        coordinates = self.rotate_object([self], Point, angle)[0]
        x, y, _ = coordinates
        self.x = x
        self.y = y

    def translation(self, Point):
        coordinates = self.translation_object([self], Point)[0]
        x, y, _ = coordinates
        self.x = x
        self.y = y

    def scale(self, scaleX, scaleY):
        coordinates = self.scale_object([self], scaleX, scaleY)[0]
        x, y, _ = coordinates
        self.x = x
        self.y = y

    def getCenter(self):
        return self
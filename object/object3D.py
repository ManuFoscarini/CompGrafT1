import numpy
from PyQt5.QtGui import QBrush, QPainterPath, QColor
from object.world import World
from PyQt5.QtCore import Qt
from operations import transform


class Object3D():
    def __init__(self, points, type, color=QColor(0, 0, 0), filled=False):
        self.points = points
        self.color = color
        self.filled = filled
        self.type = type
        self.label = "#{}: {}".format(World.numberObjects, self.type)
        self.clip = False

    def setType(self, type):
        self.type = type

    def getType(self):
        return self.type

    def setPoints(self, points):
        self.points = points

    def draw(self, painter):
        if self.clip:
            return
        path = QPainterPath()
        painter.setPen(self.color)

        if (self.type == 'Curve Bezier' or self.type == 'Curve Spline'):
            for position in range(0, len(self.points) - 1):
                x1, y1 = self.points[position]
                x2, y2 = self.points[position+1]
                painter.drawLine(x1, y1, x2, y2)
            return

        if (len(self.points) == 1):
            x, y = self.points[0]
            painter.drawPoint(x, y)
        elif (len(self.points) == 2):
            x1, y1 = self.points[0]
            x2, y2 = self.points[1]
            painter.drawLine(x1, y1, x2, y2)
        elif (len(self.points) > 2):
            if self.filled:
                painter.setBrush(QBrush(self.color, Qt.SolidPattern))
            xi, yi = self.points[0]
            path.moveTo(xi, yi)
            for point in self.points:
                x, y = point
                path.lineTo(x, y)
            path.lineTo(xi, yi)
            painter.drawPath(path)

    def rotate(self, angle, anchorPoint):
        transform.rotate_shape(self, angle, anchorPoint)

    def translation(self, anchorPoint):
        x, y = anchorPoint
        transform.translate_shape(self, x, y)

    def scale(self, scaleX, scaleY):
        transform.scale_shape(self, scaleX, scaleY)

    def getCenter(self):
        x_points = [point[0] for point in self.points]
        y_points = [point[1] for point in self.points]
        return [numpy.average(x_points), numpy.average(y_points)]

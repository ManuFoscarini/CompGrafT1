from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPainterPath, QColor
from object.transform import TransformPoint
from object.point import Point
from object.world import World


class Object(TransformPoint):
    def __init__(self, points, type, color = QColor(0, 0, 0), filled=False):
        self.points = points
        self.color = color
        self.type = type
        self.label = "#{}: {}".format(World.numberObjects, self.type)
        self.clip = False
        self.filled = filled

    def setType(self, type):
        self.type = type

    def setPoints(self, points):
        self.points = points

    def draw(self, painter):
        if self.clip:
            return
        path = QPainterPath()
        painter.setPen(self.color)

        if (self.type == 'Curve Bezier' or self.type == 'Curve Spline'):
            for position in range(0, len(self.points) - 1):
                painter.drawLine(self.points[position], self.points[position+1])
            return

        if (len(self.points) == 1):
            painter.drawPoint(self.points[0])
        elif (len(self.points) == 2):
            painter.drawLine(self.points[0], self.points[1])
        elif (len(self.points) > 2):
            if self.filled:
                painter.setBrush(QBrush(self.color, Qt.SolidPattern))
            path.moveTo(self.points[0])
            for point in self.points:
                path.lineTo(point)
            path.lineTo(self.points[0])
            painter.drawPath(path)

    def rotate(self, anchorPoint, angle):
        coordinates = self.rotate_object(self.points, anchorPoint, angle)
        wireframeRotate = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeRotate.append(Point(x, y))
        self.points = wireframeRotate

    def translation(self, anchorPoint):
        coordinates = self.translation_object(self.points, anchorPoint)
        wireframeTranslation = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeTranslation.append(Point(x, y))
        self.points = wireframeTranslation

    def scale(self, scaleX, scaleY):
        coordinates = self.scale_object(self.points, scaleX, scaleY)
        wireframeScale = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeScale.append(Point(x, y))
        self.points = wireframeScale

    def getCenter(self):
        cx, cy = self.getCenterObject(self.points)
        return Point(cx, cy)

    def normalized(self, centerPoint, angle, factor):
        coordinates = self.normalized_objects(self.points, centerPoint, angle, factor)
        wireframeCoordinates = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeCoordinates.append(Point(x, y))
        self.points = wireframeCoordinates

    def coordinatesToPoint(self, points):
        newPoints = []
        for point in points:
            x, y = point
            newPoints.append(Point(x, y))

        return newPoints

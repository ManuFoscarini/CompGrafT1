from PyQt5.QtGui import QColor
from object.transform import Object2D
from object.point import Point
from object.world import World


class Object(Object2D):
    def __init__(self, points, type, color = QColor(0, 0, 0)):
        self.points = points
        self.color = color
        self.type = type
        self.label = "#{}: {}".format(World.numberObjects, self.type)

    def setType(self, type):
        self.type = type

    def setPoints(self, points):
        self.points = points

    def draw(self, painter):
        painter.setPen(self.color)
        if (len(self.points) == 1):
            painter.drawPoint(self.points[0])
        elif (len(self.points) == 2):
            painter.drawLine(self.points[0], self.points[1])
        else:
            for position in range(0, len(self.points)):
                if(position < (len(self.points) - 1)):
                    painter.drawLine(
                        self.points[position], self.points[position+1])
                else:
                    painter.drawLine(
                        self.points[position], self.points[0])

    def rotate(self, anchorPoint, angle):
        coordinates = self.rotateObject(self.points, anchorPoint, angle)
        wireframeRotate = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeRotate.append(Point(x, y))
        self.points = wireframeRotate

    def translation(self, anchorPoint):
        coordinates = self.translationObject(self.points, anchorPoint)
        wireframeTranslation = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeTranslation.append(Point(x, y))
        self.points = wireframeTranslation

    def scale(self, scaleX, scaleY):
        coordinates = self.scaleObject(self.points, scaleX, scaleY)
        wireframeScale = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeScale.append(Point(x, y))
        self.points = wireframeScale

    def getCenter(self):
        cx, cy = self.getCenterObject(self.points)
        return Point(cx, cy)

    def normalized(self, centerPoint, angle, factor):
        coordinates = self.normalizedObjects(self.points, centerPoint, angle, factor)
        wireframeCoordinates = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeCoordinates.append(Point(x, y))
        self.points = wireframeCoordinates

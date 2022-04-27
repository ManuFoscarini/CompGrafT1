from object.transform import transform_point
from object.point import Point


class Wireframe(transform_point):
    def __init__(self, points):
        self.points = points
        self.label = "Wireframe Points: {}".format(
            self.formatPointsLabel(points))

    def formatPointsLabel(self, points):
        pointsLabel = ""
        for point in points:
            pointsLabel += "({},{}) ".format(point.x, point.y)
        return pointsLabel

    def draw(self, painter):
        transformedPoints = []
        for point in self.points:
            coordinateTransformed = self.transformViewport(point)
            pointTransformed = Point(
                coordinateTransformed[0], coordinateTransformed[1])
            transformedPoints.append(pointTransformed)

        if (len(transformedPoints) == 1):
            painter.drawPoint(transformedPoints[0])
        elif (len(transformedPoints) == 2):
            painter.drawLine(transformedPoints[0], transformedPoints[1])
        else:
            for position in range(0, len(transformedPoints)):
                if(position < (len(transformedPoints) - 1)):
                    painter.drawLine(
                        transformedPoints[position], transformedPoints[position+1])
                else:
                    painter.drawLine(
                          transformedPoints[position], transformedPoints[0])
                          
    def rotate(self, anchorPoint, angle):
        coordinates = self.rotateObject(self.points, anchorPoint, angle)
        wireframeRotate = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframeRotate.append(Point(x, y))
        self.points = wireframeRotate

    def getCenter(self):
        cx, cy = self.getCenterObject(self.points)
        return Point(cx, cy)
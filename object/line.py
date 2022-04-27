from object.transform import transform_point
from object.point import Point

class Line(transform_point):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.label = "Line Points: {}".format(
            self.formatPointsLabel([point1, point2]))

    def formatPointsLabel(self, points):
        pointsLabel = ""
        for point in points:
            pointsLabel += "({},{}) ".format(point.x, point.y)
        return pointsLabel

    def draw(self, painter):
        coord1Transformed = self.transformViewport(self.point1)
        coord2Transformed = self.transformViewport(self.point2)
        p1Transformed = Point(coord1Transformed[0], coord1Transformed[1])
        p2Transformed = Point(coord2Transformed[0], coord2Transformed[1])
        painter.drawLine(p1Transformed, p2Transformed)

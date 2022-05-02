from object.transform import TransformPoint
from object.point import Point


class Line(TransformPoint):
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        self.label = "Line Points: {}".format(
            self.format_point_labels([point1, point2]))

    @staticmethod
    def format_point_labels(points):
        point_labels = ""
        for point in points:
            point_labels += "({},{}) ".format(point.x, point.y)
        return point_labels

    def draw(self, painter):
        coord1_transformed = self.viewport_transformation(self.point1)
        coord2_transformed = self.viewport_transformation(self.point2)
        p1_transformed = Point(coord1_transformed[0], coord1_transformed[1])
        p2_transformed = Point(coord2_transformed[0], coord2_transformed[1])
        painter.drawLine(p1_transformed, p2_transformed)
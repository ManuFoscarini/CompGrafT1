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
        cordinates_transformed = self.viewport_transformation([self.point1, self.point2])
        list = []
        for cordinateTransformed in cordinates_transformed:
            list.append(Point(cordinateTransformed[0], cordinateTransformed[1]))
        painter.drawLine(list[0], list[1])
        
    def rotate(self, anchorPoint, angle):
        coord1, coord2 = self.rotate_object([self.point1, self.point2], anchorPoint, angle)
        self.point1 = Point(coord1[0], coord1[1])
        self.point2 = Point(coord2[0], coord2[1])

    def translation(self, anchorPoint):
        coord1, coord2 = self.translation_object([self.point1, self.point2], anchorPoint)
        self.point1 = Point(coord1[0], coord1[1])
        self.point2 = Point(coord2[0], coord2[1])

    def scale(self, scaleX, scaleY):
        coord1, coord2 = self.scale_object([self.point1, self.point2], scaleX, scaleY)
        self.point1 = Point(coord1[0], coord1[1])
        self.point2 = Point(coord2[0], coord2[1])

    def getCenter(self):
        cx, cy = self.getCenterObject([self.point1, self.point2])
        return Point(cx, cy)
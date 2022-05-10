from object.transform import TransformPoint
from object.point import Point


class Wireframe(TransformPoint):
    def __init__(self, points):
        self.points = points
        self.label = "Wireframe Points: {}".format(
            self.format_point_labels())

    def format_point_labels(self):
        point_labels = ""
        for point in self.points:
            point_labels += "({},{}) ".format(point.x, point.y)
        return point_labels

    def draw(self, painter):
        coordinate_transformed = self.viewport_transformation(self.points)
        transformed_points = []
        for point in coordinate_transformed:
            transformed_points.append(Point(point[0], point[1]))

        if (len(transformed_points) == 1):
            painter.drawPoint(transformed_points[0])
        elif (len(transformed_points) == 2):
            painter.drawLine(transformed_points[0], transformed_points[1])
        else:
            for position in range(0, len(transformed_points)):
                if(position < (len(transformed_points) - 1)):
                    painter.drawLine(
                        transformed_points[position], transformed_points[position+1])
                else:
                    painter.drawLine(
                        transformed_points[position], transformed_points[0])

    def rotate(self, Point, angle):
        coordinates = self.rotate_object(self.points, Point, angle)
        wireframe_rotate = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframe_rotate.append(Point(x, y))
        self.points = wireframe_rotate

    def translation(self, Point):
        coordinates = self.translation_object(self.points, Point)
        wireframe_translation = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframe_translation.append(Point(x, y))
        self.points = wireframe_translation

    def scale(self, scaleX, scaleY):
        coordinates = self.scale_object(self.points, scaleX, scaleY)
        wireframe_scale = []
        for coordinate in coordinates:
            x, y, _ = coordinate
            wireframe_scale.append(Point(x, y))
        self.points = wireframe_scale

    def getCenter(self):
        cx, cy = self.getCenterObject(self.points)
        return Point(cx, cy)
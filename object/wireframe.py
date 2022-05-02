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
        transformed_points = list()
        for point in self.points:
            coordinate_transformed = self.viewport_transformation(point)
            point_transformed = Point(
                coordinate_transformed[0], coordinate_transformed[1])
            transformed_points.append(point_transformed)

        if len(transformed_points) == 1:
            painter.drawPoint(transformed_points[0])
        elif len(transformed_points) == 2:
            painter.drawLine(transformed_points[0], transformed_points[1])
        else:
            for position in range(0, len(transformed_points)):
                if position < (len(transformed_points) - 1):
                    painter.drawLine(
                        transformed_points[position], transformed_points[position+1])
                else:
                    painter.drawLine(
                          transformed_points[position], transformed_points[0])
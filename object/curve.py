import numpy


class Curve():
    """ A Bezier curve with four control points. """
    def __init__(self, points):
        self.points = self._generate_curve(points)
        self.points.append(points[-1])

    def _generate_curve(self, points):
        def f(t, i):
            operation = numpy.array([t**3, t**2, t, 1])
            operation = operation.dot(numpy.array([
                [-1, 3, -3, 1],
                [3, -6, 3, 0],
                [-3, 3, 0, 0],
                [1, 0, 0, 0],
            ]))

            if i == 0:
                return operation.dot(numpy.array([p.x for p in points]))
            else:
                return operation.dot(numpy.array([p.y for p in points]))

        step = 0.02
        x_points = [f(t, 0) for t in numpy.arange(0, 1+step, step)]
        y_points = [f(t, 1) for t in numpy.arange(0, 1+step, step)]

        return self.makeCoordinates(x_points, y_points)

    def makeCoordinates(self, x_points, y_points):
        coordinates = []
        for i in range(0, len(x_points)):
            coordinates.append([x_points[i], y_points[i]])
        return coordinates

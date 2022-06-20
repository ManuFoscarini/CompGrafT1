import numpy


class Spline():
    """ A Spline curve with arbitrary amount of control points. """

    def __init__(self, points):
        self.points = []
        for i in range(len(points) - 3):
            # build a curve for every four control points
            self.points += self._generate_curve(points[i:i+4])

    def _generate_curve(self, points):
        coef = numpy.multiply(1/6, numpy.array([
            [-1, 3, -3, 1],
            [3, -6, 3, 0],
            [-3, 0, 3, 0],
            [1, 4, 1, 0],
        ])).dot(numpy.array(points))

        number_of_points = 50
        delta = 1/number_of_points
        deltas = numpy.array([
            [0, 0, 0, 1],
            [delta**3, delta**2, delta, 0],
            [6*delta**3, 2*delta**2, 0, 0],
            [6*delta**3, 0, 0, 0],
        ]).dot(coef)

        points = list(deltas[0])
        for _ in range(number_of_points):
            # update coordinates using forward differences
            deltas[0] += deltas[1]
            deltas[1] += deltas[2]
            deltas[2] += deltas[3]
            points.append(list(deltas[0]))
        return points
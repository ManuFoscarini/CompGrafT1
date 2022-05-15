import numpy
from object.world import World
from object.point import Point
from object.object import Object


class Window():
    width = 800
    height = 450
    BORDER = 0.05
    rotateAngle = 0
    listObjects = []

    points = [
            (0, height),
            (width, height),
            (width, 0),
            (0, 0),
        ]
    points.append(points[0])

    @staticmethod
    def normalizedObjects():
        Window.listObjects = []
        wcx, wcy = Window.center()
        for object in World.listObjects:
            rotateObject = Object(object.points, object.type, object.color)
            rotateObject.rotate(Point(wcx, wcy), numpy.radians(Window.rotateAngle))
            Window.listObjects.append(rotateObject)

    @staticmethod
    def expanded_boundaries():
        width = Window.points[1][0] - Window.points[3][0]
        height = Window.points[1][1] - Window.points[3][1]
        factor = numpy.multiply((width, height), Window.BORDER)
        return (
            numpy.subtract(Window.points[3], factor),
            numpy.add(Window.points[1], factor))

    @staticmethod
    def boundaries():
        return (Window.points[3], Window.points[1])

    @staticmethod
    def center():
        """ Center of the object. """
        x_points = [point[0] for point in set(Window.points)]
        y_points = [point[1] for point in set(Window.points)]
        return (numpy.average(x_points), numpy.average(y_points))

    @staticmethod
    def rotateWindow(angle):
        Window.rotateAngle += angle

    @staticmethod
    def move(offSet):
        newPoints = []
        for point in Window.points:
            newPoints.append(tuple(numpy.add(point, offSet)))
        Window.points = newPoints

    @staticmethod
    def zoom(factor):
        # find new window size
        minimum, maximum = Window.boundaries()
        width = maximum[0] - minimum[0]
        height = maximum[1] - minimum[1]

        if width < 10 and height < 10:
            return

        wcx, wcy = Window.center()
        # move object to center
        operation_matrix = numpy.array([
            [1, 0, 0],
            [0, 1, 0],
            [-wcx, -wcy, 1],
        ])

        # perform operation
        operation_matrix = operation_matrix.dot([
            [factor, 0, 0],
            [0, factor, 0],
            [0, 0, 1],
        ])

        # move object back to original position
        operation_matrix = operation_matrix.dot([
            [1, 0, 0],
            [0, 1, 0],
            [wcx, wcy, 1],
        ])

        newPoints = []
        for point in Window.points:
            x, y, _ = numpy.dot(operation_matrix, [point[0], point[1], 1])
            newPoints.append(tuple([x, y]))
        Window.points = newPoints

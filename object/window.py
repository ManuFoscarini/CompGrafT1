import numpy
from object.world import World
from object.object import Object2D
from operations import transform


class Window():
    BORDER = 0.05

    width = 800
    height = 450

    rotateAngle = 0
    listObjects = []

    LINECLIPPING = "CohenSutherland"

    points = [
            [0, height],
            [width, height],
            [width, 0],
            [0, 0],
        ]

    @staticmethod
    def copyListObjects(listObjects):
        newListObject = []
        for object in listObjects:
            newObject = Object2D(object.points, object.type, object.color, object.filled)
            newObject.clip = object.clip
            newListObject.append(newObject)
        return newListObject

    @staticmethod
    def normalizedObjects():
        Window.listObjects = Window.copyListObjects(World.listObjects)

        center = Window.center()
        for object in Window.listObjects:
            transform.normalize_shape(object, center, Window.rotateAngle)

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
        x_points = [point[0] for point in Window.points]
        y_points = [point[1] for point in Window.points]
        return [numpy.average(x_points), numpy.average(y_points)]

    @staticmethod
    def rotateWindow(angle):
        if(Window.rotateAngle + angle <= 90 and Window.rotateAngle + angle >= -90):
            Window.rotateAngle += angle

    @staticmethod
    def move(offSet):
        newPoints = []
        angle = numpy.radians(-Window.rotateAngle)
        offSetx, offSety = offSet
        rotateMatrix = [
            [numpy.cos(angle), -numpy.sin(angle), 0], 
            [numpy.sin(angle), numpy.cos(angle), 0], 
            [0, 0, 1]
        ]
        for point in Window.points:
            offSet = numpy.dot([offSetx, offSety, 1], rotateMatrix)
            xp, yp = point
            x, y, _ = numpy.add([xp, yp, 1], offSet)
            newPoints.append((x, y))
        Window.points = newPoints


    @staticmethod
    def zoom(factor):
        transform.scale_shape(Window, factor, factor)

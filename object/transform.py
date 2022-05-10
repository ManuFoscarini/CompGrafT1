from windows.configs import Configs
from windows.window import Window
import numpy


class TransformPoint:

    def viewport_transformation(self, points):
        listOfPoints = []
        for point in points:
            xvp = ((point.x - Window.x_min) / (Window.x_max - Window.x_min)) * (Configs.x_max - Configs.x_min)
            yvp = (1 - ( (point.y - Window.y_min) / (Window.y_max - Window.y_min) ) ) * (Configs.y_max - Configs.y_min)
            listOfPoints.append([xvp, yvp])
        return listOfPoints

    def rotate_object(self, points, Point, angle):
        rotate = []
        rotateAngle = self.getAngleInRadianus(angle)
        for point in points:
            pointMatrix = [point.x, point.y, 1]
            toCenter = [[1, 0, 0], [0, 1, 0], [-Point.x, -Point.y, 1]]
            rotatePoint = numpy.dot(pointMatrix, toCenter)
            rotateMatrix = [[numpy.cos(rotateAngle), -numpy.sin(rotateAngle), 0], [numpy.sin(rotateAngle), numpy.cos(rotateAngle), 0], [0, 0, 1]]
            rotatePoint = numpy.dot(rotatePoint, rotateMatrix)
            translateMatrixBack = [[1, 0, 0], [0, 1, 0], [Point.x, Point.y, 1]]
            rotatePoint = numpy.dot(rotatePoint, translateMatrixBack)
            rotate.append(rotatePoint)
        return rotate

    def scale_object(self, points, scaleX, scaleY):
        scale = []
        cx, cy = self.getCenterObject(points)
        for point in points:
            pointMatrix = [point.x, point.y, 1]
            toCenter = [[1, 0, 0], [0, 1, 0], [-cx, -cy, 1]]
            scalePoint = numpy.dot(pointMatrix, toCenter)
            scaleMatrix = [[scaleX, 0, 0], [0, scaleY, 0], [0, 0, 1]]
            scalePoint = numpy.dot(scalePoint, scaleMatrix)
            translateMatrixBack = [[1, 0, 0], [0, 1, 0], [cx, cy, 1]]
            scalePoint = numpy.dot(scalePoint, translateMatrixBack)
            scale.append(scalePoint)
        return scale

    def translation_object(self, points, destinationPoint):
        objectTranslation = []
        for point in points:
            pointMatrix = [point.x, point.y, 1]
            translateMatrixToCenter = [[1, 0, 0], [0, 1, 0], [destinationPoint.x, destinationPoint.y, 1]]
            translationPoint = numpy.dot(pointMatrix, translateMatrixToCenter)
            objectTranslation.append(translationPoint)
        return objectTranslation

    def getCenterObject(self, points):
        m = len(points)
        cx = 0
        cy = 0
        for point in points:
            cx += point.x
            cy += point.y
        return [(cx/m), (cy/m)]

    def getAngleInRadianus(self, angle):
        return angle * numpy.pi/180
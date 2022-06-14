import numpy
from object.world import World
from object.window import Window
from object.point import Point
from object.object import Object


class Viewport():
    xmin = 0
    xmax = 800
    ymin = 0
    ymax = 450
    listObjects = []

    @staticmethod
    def transformViewport():
        Viewport.listObjects = Window.copyListObjects(Window.listObjects)
        (xmin, ymin), (xmax, ymax) = Window.expanded_boundaries()
        for object in Viewport.listObjects:
            listPoints = []
            for point in object.points:
                xvp = ((point.x - xmin) / (xmax - xmin)) * (Viewport.xmax - Viewport.xmin)
                yvp = (1 - ((point.y - ymin) / (ymax - ymin))) * (Viewport.ymax - Viewport.ymin)
                listPoints.append(Point(xvp, yvp))
            object.points = listPoints

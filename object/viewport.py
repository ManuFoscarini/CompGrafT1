from object.window import Window


class Viewport():
    xmin = 0
    xmax = 800
    ymin = 0
    ymax = 450
    listObjects = []

    @staticmethod
    def transformViewport():
        Viewport.listObjects = Window.copyListObjects(Window.listObjects)
        [xmin, ymin], [xmax, ymax] = Window.expanded_boundaries()
        for object in Viewport.listObjects:
            listPoints = []
            for point in object.points:
                x, y = point
                xvp = ((x - xmin) / (xmax - xmin)) * (Viewport.xmax - Viewport.xmin)
                yvp = (1 - ((y - ymin) / (ymax - ymin))) * (Viewport.ymax - Viewport.ymin)
                listPoints.append([xvp, yvp])
            object.points = listPoints

import numpy
from object.world import World
from object.point import Point
from object.object import Object


class Window():
    INSIDE = 0
    LEFT = 1
    RIGHT = 2
    BOTTOM = 4
    TOP = 8
    width = 800
    height = 450
    BORDER = 0.05
    rotateAngle = 0
    listObjects = []
    LINECLIPPING = "CohenSutherland"

    points = [
            (0, height),
            (width, height),
            (width, 0),
            (0, 0),
        ]
    points.append(points[0])

    @staticmethod
    def copyListObjects(listObjects):
        newListObject = []
        for object in listObjects:
            newObject = Object(object.points, object.type, object.color, object.filled)
            newObject.clip = object.clip
            newListObject.append(newObject)
        return newListObject

    @staticmethod
    def normalizedObjects():
        Window.listObjects = Window.copyListObjects(World.listObjects)
        wcx, wcy = Window.center()
        for object in Window.listObjects:
            object.rotate(Point(wcx, wcy), numpy.radians(Window.rotateAngle))
        Window.clip()

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

    @staticmethod
    def clip():
        Window.pointClipping()
        Window.lineClipping()
        Window.curveClipping()
        Window.polygonClipping()

    @staticmethod
    def pointClipping():
        minimum, maximum = Window.boundaries()
        xmin, ymin = minimum
        xmax, ymax = maximum
        for i, object in enumerate(Window.listObjects):
            if len(object.points) == 1:
                if not(xmin <= object.points[0].x <= xmax and ymin <= object.points[0].y <= ymax):
                    Window.listObjects[i].clip = True

    @staticmethod
    def curveClipping():
        for i, object in enumerate(Window.listObjects):
            if object.type == "Curve Bezier" or object.type == "Curve Spline":
                newPoints = []
                for i in range(0, len(object.points) - 1):
                    point1 = object.points[i]
                    point2 = object.points[i+1]
                    line = [(point1.x, point1.y), (point2.x, point2.y)]
                    if(Window.LINECLIPPING == "CohenSutherland"):
                        newLine = Window.cohenSutherland(line)
                    else:
                        newLine = Window.liangBarsky(line)

                    if(newLine is not None):
                        [(x1, y1), (x2, y2)] = newLine
                        newPoints.append(Point(x1, y1))
                        newPoints.append(Point(x2, y2))
                object.points = newPoints

    @staticmethod
    def lineClipping():
        for i, object in enumerate(Window.listObjects):
            if len(object.points) == 2:
                x1 = object.points[0].x
                y1 = object.points[0].y
                x2 = object.points[1].x
                y2 = object.points[1].y
                line = [(x1, y1), (x2, y2)]
                if(Window.LINECLIPPING == "CohenSutherland"):
                    newLine = Window.cohenSutherland(line)
                else:
                    newLine = Window.liangBarsky(line)

                if(newLine is not None):
                    [(x1, y1), (x2, y2)] = newLine
                    newLine = [Point(x1, y1), Point(x2, y2)]
                    Window.listObjects[i].points = newLine
                else:
                    Window.listObjects[i].clip = True

    @staticmethod
    def polygonClipping():
        for i, object in enumerate(Window.listObjects):
            subject = []
            if len(object.points) > 2 and object.type != 'Curve Bezier' and object.type != 'Curve Spline':
                for point in object.points:
                    subject.append([point.x, point.y])
                newSubject = Window.sutherlandHodgman(subject)
                if newSubject is None:
                    Window.listObjects[i].clip = True
                else:
                    newPoints = []
                    for newPoint in newSubject:
                        newPoints.append(Point(newPoint[0], newPoint[1]))
                    object.points = newPoints

    @staticmethod
    def computeCode(point, xmin, ymin, xmax, ymax):
        [x, y] = point
        code = Window.INSIDE

        if (x < xmin):
            code |= Window.LEFT
        elif (x > xmax):
            code |= Window.RIGHT

        if (y < ymin):
            code |= Window.BOTTOM
        elif (y > ymax):
            code |= Window.TOP

        return code

    @staticmethod
    def cohenSutherland(line):
        [p0, p1] = line

        minimum, maximum = Window.boundaries()
        xmin, ymin = minimum
        xmax, ymax = maximum

        codeLineStart = Window.computeCode(p0, xmin, ymin, xmax, ymax)
        codeLineEnd = Window.computeCode(p1, xmin, ymin, xmax, ymax)

        while(True):
            outcodeOut = codeLineEnd if codeLineEnd > codeLineStart else codeLineStart
            if not (codeLineStart | codeLineEnd):
                return line
            elif (codeLineStart & codeLineEnd):
                return None
            else:
                [(x0, y0), (x1, y1)] = line
                x_new = None
                y_new = None

                if outcodeOut & Window.TOP:
                    x_new = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                    y_new = ymax
                elif outcodeOut & Window.BOTTOM:
                    x_new = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                    y_new = ymin
                elif outcodeOut & Window.RIGHT:
                    y_new = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                    x_new = xmax
                elif outcodeOut & Window.LEFT:
                    y_new = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                    x_new = xmin

            if(outcodeOut == codeLineStart):
                line[0] = (x_new, y_new)
                codeLineStart = Window.computeCode(line[0], xmin, ymin, xmax, ymax)
            else:
                line[1] = (x_new, y_new)
                codeLineEnd = Window.computeCode(line[1], xmin, ymin, xmax, ymax)

    @staticmethod
    def liangBarsky(line):
        minimum, maximum = Window.boundaries()
        xmin, ymin = minimum
        xmax, ymax = maximum
        [(x1, y1), (x2, y2)] = line
        t = [None, None, None, None]
        p = [-(x2 - x1), x2 - x1, -(y2 - y1), y2 - y1]
        q = [x1 - xmin, xmax - x1, y1 - ymin, ymax - y1]
        t1 = 0
        t2 = 1
        for i in range(0, 4):
            if p[i] > 0:
                t[i] = q[i] / p[i]
                t2 = min(t2, t[i])
            elif p[i] < 0:
                t[i] = q[i] / p[i]
                t1 = max(t1, t[i])
            elif q[i] < 0:
                return None
        if t1 == 0 and t2 == 0:
            return line
        if t1 < t2:
            return [(x1 + t1 * p[1], y1 + t1 * p[3]), (x1 + t2 * p[1], y1 + t2 * p[3])]
        else:
            return None

    @staticmethod
    def sutherlandHodgman(subject):
        minimum, maximum = Window.boundaries()
        xmin, ymin = minimum
        xmax, ymax = maximum
        clip = [(xmin, ymax), (xmin, ymin), (xmax, ymin), (xmax, ymax)]

        def inside(p, cp0, cp1):
            [x, y] = p
            [x0, y0] = cp0
            [x1, y1] = cp1

            return (x1 - x0) * (y - y0) > (y1 - y0) * (x - x0)

        def intersect(p1, p2, cp0, cp1):
            [x0, y0] = cp0
            [x1, y1] = cp1

            dc = (x0 - x1, y0 - y1)
            dp = (p1[0] - p2[0], p1[1] - p2[1])
            n1 = x0 * y1 - y0 * x1
            n2 = p1[0] * p2[1] - p1[1] * p2[0]
            n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0])
            return ((n1 * dp[0] - n2 * dc[0]) * n3, (n1 * dp[1] - n2 * dc[1]) * n3)

        output = subject.copy()
        cp0 = clip[-1]
        for clip_vertex in clip:
            cp1 = clip_vertex
            inputList = output
            output = []

            # Polygon out of window, do not draw
            if len(inputList) == 0:
                return None

            s = inputList[-1]
            for subjectVertex in inputList:
                e = subjectVertex
                if inside(e, cp0, cp1):
                    if not inside(s, cp0, cp1):
                        output.append(intersect(s, e, cp0, cp1))
                    output.append(e)
                elif inside(s, cp0, cp1):
                    output.append(intersect(s, e, cp0, cp1))
                s = e
            cp0 = cp1
        return output
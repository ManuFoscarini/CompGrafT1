from object.window import Window


class Clipping:
    INSIDE = 0
    LEFT = 1
    RIGHT = 2
    BOTTOM = 4
    TOP = 8

    def clip(self, listObjects):
        self.pointClipping(listObjects)
        self.lineClipping(listObjects)
        self.curveClipping(listObjects)
        self.polygonClipping(listObjects)

    def pointClipping(self, listObjects):
        minimum, maximum = Window.boundaries()
        xmin, ymin = minimum
        xmax, ymax = maximum
        for i, object in enumerate(listObjects):
            if len(object.points) == 1:
                x, y = object.points[0]
                if not(xmin <= x <= xmax and ymin <= y <= ymax):
                    listObjects[i].clip = True

    def curveClipping(self, listObjects):
        for i, object in enumerate(listObjects):
            if object.type == "Curve Bezier" or object.type == "Curve Spline":
                newPoints = []
                for i in range(0, len(object.points) - 1):
                    point1 = object.points[i]
                    point2 = object.points[i+1]
                    line = [point1, point2]
                    if(Window.LINECLIPPING == "CohenSutherland"):
                        newLine = self.cohenSutherland(line)
                    else:
                        newLine = self.liangBarsky(line)

                    if(newLine is not None):
                        [[x1, y1], [x2, y2]] = newLine
                        newPoints.append([x1, y1])
                        newPoints.append([x2, y2])
                object.points = newPoints

    def lineClipping(self, listObjects):
        for i, object in enumerate(listObjects):
            if len(object.points) == 2:
                x1, y1 = object.points[0]
                x2, y2 = object.points[1]
                line = [[x1, y1], [x2, y2]]
                if(Window.LINECLIPPING == "CohenSutherland"):
                    newLine = self.cohenSutherland(line)
                else:
                    newLine = self.liangBarsky(line)

                if(newLine is not None):
                    listObjects[i].points = newLine
                else:
                    listObjects[i].clip = True

    def polygonClipping(self, listObjects):
        for i, object in enumerate(listObjects):
            subject = []
            if len(object.points) > 2 and object.type != 'Curve Bezier' and object.type != 'Curve Spline':
                for point in object.points:
                    x, y = point
                    subject.append([x, y])
                newSubject = self.sutherlandHodgman(subject)
                if newSubject is None:
                    listObjects[i].clip = True
                else:
                    newPoints = []
                    for newPoint in newSubject:
                        x, y = newPoint
                        newPoints.append([x, y])
                    object.points = newPoints

    def computeCode(self, point, xmin, ymin, xmax, ymax):
        [x, y] = point
        code = self.INSIDE

        if (x < xmin):
            code |= self.LEFT
        elif (x > xmax):
            code |= self.RIGHT

        if (y < ymin):
            code |= self.BOTTOM
        elif (y > ymax):
            code |= self.TOP

        return code

    def cohenSutherland(self, line):
        [p0, p1] = line

        minimum, maximum = Window.boundaries()
        xmin, ymin = minimum
        xmax, ymax = maximum

        codeLineStart = self.computeCode(p0, xmin, ymin, xmax, ymax)
        codeLineEnd = self.computeCode(p1, xmin, ymin, xmax, ymax)

        while(True):
            outcodeOut = codeLineEnd if codeLineEnd > codeLineStart else codeLineStart
            if not (codeLineStart | codeLineEnd):
                return line
            elif (codeLineStart & codeLineEnd):
                return None
            else:
                [[x0, y0], [x1, y1]] = line
                x_new = None
                y_new = None

                if outcodeOut & self.TOP:
                    x_new = x0 + (x1 - x0) * (ymax - y0) / (y1 - y0)
                    y_new = ymax
                elif outcodeOut & self.BOTTOM:
                    x_new = x0 + (x1 - x0) * (ymin - y0) / (y1 - y0)
                    y_new = ymin
                elif outcodeOut & self.RIGHT:
                    y_new = y0 + (y1 - y0) * (xmax - x0) / (x1 - x0)
                    x_new = xmax
                elif outcodeOut & self.LEFT:
                    y_new = y0 + (y1 - y0) * (xmin - x0) / (x1 - x0)
                    x_new = xmin

            if(outcodeOut == codeLineStart):
                line[0] = [x_new, y_new]
                codeLineStart = self.computeCode(line[0], xmin, ymin, xmax, ymax)
            else:
                line[1] = [x_new, y_new]
                codeLineEnd = self.computeCode(line[1], xmin, ymin, xmax, ymax)

    def liangBarsky(self, line):
        minimum, maximum = Window.boundaries()
        xmin, ymin = minimum
        xmax, ymax = maximum
        [[x1, y1], [x2, y2]] = line
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
            return [[x1 + t1 * p[1], y1 + t1 * p[3]], [x1 + t2 * p[1], y1 + t2 * p[3]]]
        else:
            return None

    def sutherlandHodgman(self, subject):
        minimum, maximum = Window.boundaries()
        xmin, ymin = minimum
        xmax, ymax = maximum
        clip = [[xmin, ymax], [xmin, ymin], [xmax, ymin], [xmax, ymax]]

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
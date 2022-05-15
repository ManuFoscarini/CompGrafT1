from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPalette, QColor
from PyQt5 import QtCore
from object.viewport import Viewport
from object.window import Window
from object.point import Point
from PyQt5.QtGui import QPen
from PyQt5.QtCore import Qt
from dataclasses import dataclass

(xmin, ymin), (xmax, ymax) = Window.expanded_boundaries()
xini = ((0 - xmin) / (xmax - xmin)) * (Viewport.xmax - Viewport.xmin)
yini = (1 - ((0 - ymin) / (ymax - ymin))) * (Viewport.ymax - Viewport.ymin)
xfin = ((800 - xmin) / (xmax - xmin)) * (Viewport.xmax - Viewport.xmin)
yfin = (1 - ((450 - ymin) / (ymax - ymin))) * (Viewport.ymax - Viewport.ymin)
rect = QRectF(Point(xini, yini), Point(xfin, yfin))


class ViewPort(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(Viewport.xmax, Viewport.ymax)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('light gray'))
        self.setPalette(palette)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000/60)

    def paintEvent(self, event):
        painter = QPainter(self)

        Window.normalizedObjects()
        Viewport.transformViewport()

        #red_pen_for(painter)
        #green_pen_for(painter)

        for object in Viewport.listObjects:
            object.draw(painter)

    @dataclass
    class YAxis:
        x1: float = 0
        y1: float = 0
        x2: float = 0
        y2: float = 800

    @dataclass
    class XAxis:
        x1: float = 0
        y1: float = 450
        x2: float = 800
        y2: float = 450

def red_pen_for(painter):
    pen = QPen(Qt.red, 3, Qt.SolidLine)
    painter.setPen(pen)
    painter.drawLine(
        ViewPort.YAxis.x1,
        ViewPort.YAxis.y1,
        ViewPort.YAxis.x2,
        ViewPort.YAxis.y2)


def green_pen_for(painter):
    pen = QPen(Qt.green, 3, Qt.SolidLine)
    painter.setPen(pen)
    painter.drawLine(
        ViewPort.XAxis.x1,
        ViewPort.XAxis.y1,
        ViewPort.XAxis.x2,
        ViewPort.XAxis.y2)

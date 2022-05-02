from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPalette, QColor
from PyQt5 import QtCore
from object.objects import Objects
from windows.configs import Configs
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt
from dataclasses import dataclass


class ViewPort(QWidget):

    def __init__(self):
        super().__init__()
        self.setGeometry(200, 0, Configs.x_max, Configs.y_max)
        self.setFixedSize(Configs.x_max, Configs.y_max)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('light gray'))
        self.setPalette(palette)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 / 40)

    def paintEvent(self, event):
        painter = QPainter(self)

        red_pen_for(painter)
        green_pen_for(painter)
        black_pen_for(painter)

        for o in Objects.listObjects:
            o.draw(painter)

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
    pen = QPen(Qt.red, 4, Qt.SolidLine)
    painter.setPen(pen)
    painter.drawLine(
        ViewPort.YAxis.x1,
        ViewPort.YAxis.y1,
        ViewPort.YAxis.x2,
        ViewPort.YAxis.y2)


def green_pen_for(painter):
    pen = QPen(Qt.green, 4, Qt.SolidLine)
    painter.setPen(pen)
    painter.drawLine(
        ViewPort.XAxis.x1,
        ViewPort.XAxis.y1,
        ViewPort.XAxis.x2,
        ViewPort.XAxis.y2)


def black_pen_for(painter):
    pen = QPen(Qt.black, 2, Qt.SolidLine)
    painter.setPen(pen)
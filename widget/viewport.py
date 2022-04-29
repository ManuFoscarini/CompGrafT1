from turtle import color
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPalette, QColor
from PyQt5 import QtCore
from object.objects import Objects
from windows.configs import Configs
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class ViewPort(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 0, Configs.xmax, Configs.ymax)
        self.setFixedSize(Configs.xmax, Configs.ymax)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('light gray'))
        self.setPalette(palette)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000/40)

    def paintEvent(self, event):
        painter = QPainter(self)

        pen = QPen(Qt.red, 4, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, 0, 0, 800)

        pen = QPen(Qt.green, 4, Qt.SolidLine)
        painter.setPen(pen)
        painter.drawLine(0, 450, 800, 450)

        pen = QPen(Qt.black, 2, Qt.SolidLine)
        painter.setPen(pen)

        for object in Objects.listObjects:
            object.draw(painter)

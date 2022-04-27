from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QPainter, QPalette, QColor
from PyQt5 import QtCore
from object.objects import Objects
from windows.configs import Configs


class ViewPort(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200, 0, Configs.xmax, Configs.ymax)
        self.setFixedSize(Configs.xmax, Configs.ymax)
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor('white'))
        self.setPalette(palette)

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 / 60)

    def paintEvent(self, event):
        painter = QPainter(self)
        for object in Objects.listObjects:
            object.draw(painter)

import sys

from PyQt5.QtWidgets import QListWidget, QWidget, QVBoxLayout, QLabel
from PyQt5 import QtCore
from object.objects import Objects


class ObjectsList(QWidget):

    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)

        self.listWidget = QListWidget()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.render_objects)
        self.timer.start(1000)

        vbox.addWidget(QLabel('Objects:'))
        vbox.addWidget(self.listWidget)

    def render_objects(self):
        objects = Objects.listObjects
        self.listWidget.clear()

        for o in objects:
            self.listWidget.addItem(o.label)
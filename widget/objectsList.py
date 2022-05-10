import sys
from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QVBoxLayout, QLabel, QWidget
from PyQt5 import QtCore
from object.objects import Objects
from object.transform import *
from widget.tranformation2D import Transformation2D


class ObjectsList(QWidget):

    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)
        self.listWidget = QListWidget()
        self.objectListRendered = []
        self.transformationWidget = None

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.render_objects)
        self.timer.start(1000)

        self.listWidget.itemDoubleClicked.connect(self.launch_transformation)
        vbox.addWidget(QLabel('Objects:'))
        vbox.addWidget(self.listWidget)

    def render_objects(self):
        if(Objects.listObjects == self.objectListRendered):
            return
        self.listWidget.clear()
        for o in Objects.listObjects:
            listWidgetItem = QListWidgetItem(o.label)
            self.listWidget.addItem(listWidgetItem)
        self.objectListRendered = Objects.listObjects.copy()

    def launch_transformation(self, item):
        Objects.select_object(item.text())
        if (self.transformationWidget is None):
            self.transformationWidget = Transformation2D()
        self.transformationWidget.show()
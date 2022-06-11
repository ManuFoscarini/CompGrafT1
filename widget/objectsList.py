import sys

from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QWidget, QVBoxLayout, QLabel
from PyQt5 import QtCore
from widget.transformation2D import Transformation
from object.world import World


class ObjectsList(QWidget):

    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)
        self.listWidget = QListWidget()
        self.objectListRendered = []
        self.transformationWidget = None

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.renderObjectList)
        self.timer.start(1000 / 60)

        self.listWidget.itemDoubleClicked.connect(self.launchTransformationWidget)
        vbox.addWidget(QLabel('Objects:'))
        vbox.addWidget(self.listWidget)

    def renderObjectList(self):
        if(World.listObjects == self.objectListRendered):
            return
        self.listWidget.clear()
        for object in World.listObjects:
            listWidgetItem = QListWidgetItem(object.label)
            self.listWidget.addItem(listWidgetItem)
        self.objectListRendered = World.listObjects.copy()

    def selectObject(self, item):
        World.select_object(item.text())

    def launchTransformationWidget(self, item):
        World.select_object(item.text())
        if (self.transformationWidget is None):
            self.transformationWidget = Transformation()
        self.transformationWidget.show()

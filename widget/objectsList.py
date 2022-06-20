import sys

from PyQt5.QtWidgets import QListWidget, QListWidgetItem, QWidget, QVBoxLayout, QLabel
from PyQt5 import QtCore
from object.world import World
from widget.transformation2D import Transformation
from widget.transformation3D import TransformationWidget3D


class ObjectsList(QWidget):

    def __init__(self):
        super().__init__()
        vbox = QVBoxLayout(self)
        self.listWidget = QListWidget()
        self.objectListRendered = []
        self.transformationWidget = None
        self.transformationWidget3D = None

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.renderObjectList)
        self.timer.start(1000 / 60)

        self.listWidget.itemClicked.connect(self.selectObject)
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
        World.selectObject(item.text())

    def launchTransformationWidget(self, item):
        World.selectObject(item.text())
        tipo = World.selectedObject.getType()
        print(tipo)
        if tipo == "object3D":
            if (self.transformationWidget3D is None):
                self.transformationWidget3D = TransformationWidget3D()
            self.transformationWidget3D.show()
        else:
            if (self.transformationWidget is None):
                self.transformationWidget = Transformation()
            self.transformationWidget.show()

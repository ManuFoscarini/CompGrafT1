import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor
from object.world import World
from object.point import Point
from object.object import Object


class CoordinatesWidgetPonto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ponto")
        self.setGeometry(300, 300, 200, 100)
        layout = QVBoxLayout()

        self.coordenadaX = QLineEdit()
        self.coordenadaY = QLineEdit()
        self.colorPoint = QLineEdit()

        layout.addWidget(QLabel('X:'))
        layout.addWidget(self.coordenadaX)
        layout.addWidget(QLabel('Y:'))
        layout.addWidget(self.coordenadaY)
        layout.addWidget(QLabel('Cor: r,g,b (0 - 255)'))
        layout.addWidget(self.colorPoint)

        self.Confirma = QPushButton('Ok')
        self.Confirma.setStyleSheet('font-size: 12px')
        layout.addWidget(self.Confirma)
        self.Confirma.clicked.connect(self.printXeY)

        self.Limpar = QPushButton('Limpar')
        self.Limpar.setStyleSheet('font-size: 12px')
        layout.addWidget(self.Limpar)
        self.Limpar.clicked.connect(self.clearLabels)
        self.setLayout(layout)

    def printXeY(self):
        if (self.coordenadaX.displayText() == "" or self.coordenadaY.displayText() == ""):
            return
        x = int(self.coordenadaX.displayText())
        y = int(self.coordenadaY.displayText())
        if (self.colorPoint.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorPoint.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
        point = Point(x, y)
        newObject = Object([point], 'Point', color, False)
        World.add(newObject)
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaX.clear()
        self.coordenadaY.clear()
        self.colorPoint.clear()
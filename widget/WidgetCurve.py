import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor
from object.transform import TransformPoint
from object.world import World
from object.point import Point
from object.object import Object
from object.curve import Curve


class WidgetCurve(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Curve")
        self.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()

        self.coordenadaXY = QLineEdit()
        self.colorCurve = QLineEdit()

        self.layout.addWidget(QLabel('Todas as coordenada X e Y: x1,y1;x2,y2;x3,y3;x4,y4'))
        self.layout.addWidget(self.coordenadaXY)
        self.layout.addWidget(QLabel('Cor: r,g,b (0 - 255)'))
        self.layout.addWidget(self.colorCurve)

        self.Confirma = QPushButton('Ok')
        self.Confirma.setStyleSheet('font-size: 15px')
        self.layout.addWidget(self.Confirma)
        self.Confirma.clicked.connect(self.printXeY)
        self.setLayout(self.layout)

        self.limpar = QPushButton('Limpar')
        self.limpar.setStyleSheet('font-size: 15px')
        self.layout.addWidget(self.limpar)
        self.limpar.clicked.connect(self.clearLabels)
        self.setLayout(self.layout)

    def printXeY(self):
        newpontos = []
        coordenadasXY = self.coordenadaXY.displayText().strip().split(';')
        for stringPonto in coordenadasXY:
            if(stringPonto != ''):
                x, y = stringPonto.split(',')
                newpontos.append(Point(int(x), int(y)))
        if (self.colorCurve.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorCurve.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
        curve = Curve(newpontos)
        World.add(Object(curve.points, 'Curve Bezier', color))
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaXY.clear()
        self.colorCurve.clear()
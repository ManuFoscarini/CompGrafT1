import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor
from object.world import World
from object.point import Point
from object.object import Object


class CoordinatesWidgetPoligono(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wireframe")
        self.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()

        self.coordenadaXY = QLineEdit()
        self.colorPoligono = QLineEdit()

        self.layout.addWidget(QLabel('Todas as coordenada X e Y: x1,y1;x2,y2'))
        self.layout.addWidget(self.coordenadaXY)
        self.layout.addWidget(QLabel('Color: r,g,b (0 - 255)'))
        self.layout.addWidget(self.colorPoligono)

        self.Confirma = QPushButton('Ok')
        self.Confirma.setStyleSheet('font-size: 12px')
        self.layout.addWidget(self.Confirma)
        self.Confirma.clicked.connect(self.printXeY)
        self.setLayout(self.layout)

        self.limpar = QPushButton('Limpar')
        self.limpar.setStyleSheet('font-size: 12px')
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
        if (self.colorPoligono.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorPoligono.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
        World.addObject(Object(newpontos, "Wireframe", color))
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaXY.clear()
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor
from object.world import World
from object.point import Point
from object.spline import Spline
from object.object import Object




class WidgetSpline(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Spline")
        self.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()

        self.coordenadaXY = QLineEdit()
        self.colorSpline = QLineEdit()

        self.layout.addWidget(QLabel('Todas as coordenada X e Y (No minimo 4 pontos): x1,y1;x2,y2;x3,y3;x4,y4'))
        self.layout.addWidget(self.coordenadaXY)
        self.layout.addWidget(QLabel('Color: r,g,b (between 0 and 255)'))
        self.layout.addWidget(self.colorSpline)

        self.Confirma = QPushButton('Confirmar')
        self.Confirma.setStyleSheet('font-size: 30px')
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
        if (self.colorSpline.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorSpline.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
    
        spline = Spline(newpontos)
        World.add(Object(spline.points, 'Curve Spline', color))
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaXY.clear()
        self.colorSpline.clear()
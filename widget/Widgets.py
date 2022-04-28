from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from object.objects import Objects
from object.point import Point
from object.wireframe import Wireframe
from object.line import Line

class CoordinatesWidgetPonto(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ponto")
        self.setGeometry(300, 300, 200, 100)
        layout = QVBoxLayout()

        self.coordenadaX = QLineEdit()
        self.coordenadaY = QLineEdit()

        layout.addWidget(QLabel('X:'))
        layout.addWidget(self.coordenadaX)
        layout.addWidget(QLabel('Y:'))
        layout.addWidget(self.coordenadaY)

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
        x = int(self.coordenadaX.displayText())
        y = int(self.coordenadaY.displayText())
        point = Point(x, y)
        Objects.addObject(point)
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaX.clear()
        self.coordenadaY.clear()

class CoordinatesWidgetWireframe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Wireframe")
        self.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()

        self.coordenadaXY = QLineEdit()

        self.layout.addWidget(QLabel('Todas as coordenada X e Y: x1,y1;x2,y2'))
        self.layout.addWidget(self.coordenadaXY)

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
        Objects.addObject(Wireframe(newpontos))
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaXY.clear()

class CoordinatesWidgetLinha(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Linha")
        self.setGeometry(300, 300, 200, 100)
        layout = QVBoxLayout()

        self.coordenadaX1 = QLineEdit()
        self.coordenadaY1 = QLineEdit()
        self.coordenadaX2 = QLineEdit()
        self.coordenadaY2 = QLineEdit()

        layout.addWidget(QLabel('X1:'))
        layout.addWidget(self.coordenadaX1)
        layout.addWidget(QLabel('Y1:'))
        layout.addWidget(self.coordenadaY1)
        layout.addWidget(QLabel('X2:'))
        layout.addWidget(self.coordenadaX2)
        layout.addWidget(QLabel('Y2:'))
        layout.addWidget(self.coordenadaY2)

        self.Confirma = QPushButton('Ok')
        self.Confirma.setStyleSheet('font-size: 12px')
        layout.addWidget(self.Confirma)
        self.Confirma.clicked.connect(self.printXeY)
        self.setLayout(layout)

        self.limpar = QPushButton('Limpar')
        self.limpar.setStyleSheet('font-size: 12px')
        layout.addWidget(self.limpar)
        self.limpar.clicked.connect(self.clearLabels)
        self.setLayout(layout)

    def printXeY(self):
        x1 = int(self.coordenadaX1.displayText())
        y1 = int(self.coordenadaY1.displayText())
        ponto1 = Point(x1, y1)
        x2 = int(self.coordenadaX2.displayText())
        y2 = int(self.coordenadaY2.displayText())
        ponto2 = Point(x2, y2)
        line = Line(ponto1, ponto2)
        Objects.addObject(line)
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaX1.clear()
        self.coordenadaY1.clear()
        self.coordenadaX2.clear()
        self.coordenadaY2.clear()


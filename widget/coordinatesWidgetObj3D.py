from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel, QCheckBox
from PyQt5.QtGui import QColor
from object.world import World
from object.object3D import Object3D


class CoordinatesWidgetObj3D(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Object 3D")
        self.setGeometry(300, 300, 200, 100)
        self.layout = QVBoxLayout()

        self.coordenadaXYZ = QLineEdit()
        self.colorPoligono = QLineEdit()

        self.layout.addWidget(QLabel('Todas as coordenada X, Y e Z: x1,y1,z1;x2,y2,z2'))
        self.layout.addWidget(self.coordenadaXYZ)
        self.layout.addWidget(QLabel('Color: r,g,b (between 0 and 255)'))
        self.layout.addWidget(self.colorPoligono)

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
        coordenadasXYZ = self.coordenadaXYZ.displayText().strip().split(';')
        for stringPonto in coordenadasXYZ:
            if(stringPonto != ''):
                x, y, z = stringPonto.split(',')
                newpontos.append([float(x), float(y), float(z)])
        if (self.colorPoligono.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorPoligono.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
        World.addObject(Object3D(newpontos, "Wireframe", color, False))
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaXYZ.clear()
        self.colorPoligono.clear()

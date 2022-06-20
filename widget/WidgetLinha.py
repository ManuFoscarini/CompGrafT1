from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QVBoxLayout, QLabel
from PyQt5.QtGui import QColor
from object.world import World
from object.object import Object2D


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
        self.colorLine = QLineEdit()

        layout.addWidget(QLabel('X1:'))
        layout.addWidget(self.coordenadaX1)
        layout.addWidget(QLabel('Y1:'))
        layout.addWidget(self.coordenadaY1)
        layout.addWidget(QLabel('X2:'))
        layout.addWidget(self.coordenadaX2)
        layout.addWidget(QLabel('Y2:'))
        layout.addWidget(self.coordenadaY2)
        layout.addWidget(QLabel('Cor: r,g,b (0 - 255)'))
        layout.addWidget(self.colorLine)

        self.Confirma = QPushButton('Ok')
        self.Confirma.setStyleSheet('font-size: 15px')
        layout.addWidget(self.Confirma)
        self.Confirma.clicked.connect(self.printXeY)
        self.setLayout(layout)

        self.limpar = QPushButton('Limpar')
        self.limpar.setStyleSheet('font-size: 15px')
        layout.addWidget(self.limpar)
        self.limpar.clicked.connect(self.clearLabels)
        self.setLayout(layout)

    def printXeY(self):
        if (self.coordenadaX1.displayText() == "" or self.coordenadaY1.displayText() == "" or
                self.coordenadaX2.displayText() == "" or self.coordenadaY2.displayText() == ""):
            return
        if (self.colorLine.displayText() == ""):
            r, g, b = 0, 0, 0
            color = QColor(int(r), int(g), int(b))
        else:
            r, g, b = self.colorLine.displayText().strip().split(',')
            color = QColor(int(r), int(g), int(b))
        x1 = int(self.coordenadaX1.displayText())
        y1 = int(self.coordenadaY1.displayText())
        ponto1 = [x1, y1]
        x2 = int(self.coordenadaX2.displayText())
        y2 = int(self.coordenadaY2.displayText())
        ponto2 = [x2, y2]
        line = Object2D([ponto1, ponto2], "Line", color, False)
        World.addObject(line)
        self.close()
        self.clearLabels()

    def clearLabels(self):
        self.coordenadaX1.clear()
        self.coordenadaY1.clear()
        self.coordenadaX2.clear()
        self.coordenadaY2.clear()
        self.colorLine.clear()

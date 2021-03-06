import numpy
from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QGridLayout, QLineEdit, QLabel
from object.world import World


class Transformation(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transformações 2D")
        self.setGeometry(1225, 300, 400, 300)
        layout = QGridLayout()
        self.coordenadaX = QLineEdit()
        self.labelCoordX = QLabel('Âncora X:')

        self.coordenadaY = QLineEdit()
        self.labelCoordY = QLabel('Âncora Y:')

        self.angle = QLineEdit()
        self.angleLabel = QLabel('Ângulo:')

        self.RotateWithPoint = QPushButton('Em torno do ponto informado')
        self.RotateWithPoint.setStyleSheet('font-size: 15px')
        self.RotateWithPoint.clicked.connect(self.rotateAroundPoint)

        self.RotateCenter = QPushButton('Em torno do centro do objeto')
        self.RotateCenter.setStyleSheet('font-size: 15px')
        self.RotateCenter.clicked.connect(self.rotateAroundCenter)

        self.RotateOrigin = QPushButton('Em torno do centro do mundo')
        self.RotateOrigin.setStyleSheet('font-size: 15px')
        self.RotateOrigin.clicked.connect(self.rotateAroundOrigin)

        self.ClearLabels = QPushButton('Limpar')
        self.ClearLabels.setStyleSheet('font-size: 15px')
        self.ClearLabels.clicked.connect(self.clearLabelsRotation)

        # Translação

        self.pointX = QLineEdit()
        self.labelPointX = QLabel('Translação X:')

        self.pointY = QLineEdit()
        self.labelPointY = QLabel('Translação Y:')

        self.Translation = QPushButton('Translação')
        self.Translation.setStyleSheet('font-size: 15px')
        self.Translation.clicked.connect(self.translationAroundPoint)

        self.ClearLabelsTranslationButton = QPushButton('Limpar')
        self.ClearLabelsTranslationButton.setStyleSheet('font-size: 15px')
        self.ClearLabelsTranslationButton.clicked.connect(self.clearLabelsTranslation)

        # Escalonamento Natural

        self.scaleX = QLineEdit()
        self.labelScaleX = QLabel('Escala em X:')

        self.scaleY = QLineEdit()
        self.labelScaleY = QLabel('Escala em Y:')

        self.Scale = QPushButton('Escalonar')
        self.Scale.setStyleSheet('font-size: 15px')
        self.Scale.clicked.connect(self.scaling)

        self.ClearLablesScale = QPushButton('Limpar')
        self.ClearLablesScale.setStyleSheet('font-size: 15px')
        self.ClearLablesScale.clicked.connect(self.clearLabelsScale)

        # END OF CREATIONS OF WIDGETS START OF LAYOUT ADDING
        layout.addWidget(self.labelCoordX, 0, 0)
        layout.addWidget(self.coordenadaX, 1, 0)
        layout.addWidget(self.labelCoordY, 2, 0)
        layout.addWidget(self.coordenadaY, 3, 0)
        layout.addWidget(self.angleLabel, 4, 0)
        layout.addWidget(self.angle, 5, 0)
        layout.addWidget(self.RotateWithPoint, 6, 0)
        layout.addWidget(self.RotateCenter, 7, 0)
        layout.addWidget(self.RotateOrigin, 8, 0)
        layout.addWidget(self.ClearLabels, 9, 0)

        # END OF ADDWIDGET FOR ROTATION START OF TRANSLATION
        layout.addWidget(self.labelPointX, 0, 1)
        layout.addWidget(self.pointX, 1, 1)
        layout.addWidget(self.labelPointY, 2, 1)
        layout.addWidget(self.pointY, 3, 1)
        layout.addWidget(self.Translation, 4, 1)
        layout.addWidget(self.ClearLabelsTranslationButton, 5, 1)

        # END OF ADDWIDGET FOR TRANSLATION START OF SCALE
        layout.addWidget(self.labelScaleX, 0, 2)
        layout.addWidget(self.scaleX, 1, 2)
        layout.addWidget(self.labelScaleY, 2, 2)
        layout.addWidget(self.scaleY, 3, 2)
        layout.addWidget(self.Scale, 4, 2)
        layout.addWidget(self.ClearLablesScale, 5, 2)
        self.setLayout(layout)

    def rotateAroundPoint(self):
        if (World.selectedObject is not None):
            if (self.coordenadaX.displayText() == "" or self.coordenadaY.displayText() == "" or self.angle.displayText() == ""):
                return
            x = int(self.coordenadaX.displayText())
            y = int(self.coordenadaY.displayText())
            angle = int(self.angle.displayText())
            anchorPoint = [x, y]
            World.selectedObject.rotate(angle, anchorPoint)

    def rotateAroundCenter(self):
        if (World.selectedObject is not None):
            if (self.angle.displayText() == ""):
                return
            angle = numpy.int(self.angle.displayText())
            center = World.selectedObject.getCenter()
            World.selectedObject.rotate(angle, center)

    def rotateAroundOrigin(self):
        if (World.selectedObject is not None):
            if (self.angle.displayText() == ""):
                return
            angle = int(self.angle.displayText())
            origin = [0, 0]
            World.selectedObject.rotate(angle, origin)

    def translationAroundPoint(self):
        if (World.selectedObject is not None):
            if (self.pointX.displayText() == "" or self.pointY.displayText() == ""):
                return
            x = int(self.pointX.displayText())
            y = int(self.pointY.displayText())
            point = [x, y]
            World.selectedObject.translation(point)

    def scaling(self):
        if (World.selectedObject is not None):
            if (self.scaleX.displayText() == "" or self.scaleY.displayText() == ""):
                return
            x = float(self.scaleX.displayText())
            y = float(self.scaleY.displayText())
            World.selectedObject.scale(x, y)

    def clearLabelsRotation(self):
        self.coordenadaX.clear()
        self.coordenadaY.clear()
        self.angle.clear()

    def clearLabelsTranslation(self):
        self.pointX.clear()
        self.pointY.clear()
        self.angle.clear()

    def clearLabelsScale(self):
        self.scaleX.clear()
        self.scaleY.clear()
        self.angle.clear()
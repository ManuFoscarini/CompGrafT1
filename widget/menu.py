from PyQt5.QtWidgets import QPushButton, QWidget, QFileDialog
from widget.WidgetPonto import CoordinatesWidgetPonto
from widget.WidgetLinha import CoordinatesWidgetLinha
from widget.WidgetWireframe import CoordinatesWidgetPoligono
from object.window import Window
from object.world import World
from object.object import Object


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.coordinatesWidgetLinha = None
        self.coordinatesWidgetPonto = None  
        self.coordinatesWidgetPoligono = None  
        self.buttonUp = QPushButton("↑", self)
        self.buttonUp.clicked.connect(self.moveUp)
        self.buttonUp.setGeometry(43, 30, 86, 25)
        self.buttonLeft = QPushButton("←", self)
        self.buttonLeft.clicked.connect(self.moveLeft)
        self.buttonLeft.setGeometry(0, 55, 86, 25)
        self.buttonRight = QPushButton("→", self)
        self.buttonRight.clicked.connect(self.moveRight)
        self.buttonRight.setGeometry(86, 55, 86, 25)
        self.buttonDown = QPushButton("↓", self)
        self.buttonDown.clicked.connect(self.moveDown)
        self.buttonDown.setGeometry(43, 80, 86, 25)
        self.buttonZoomIn = QPushButton("+", self)
        self.buttonZoomIn.clicked.connect(self.zoomIn)
        self.buttonZoomIn.setGeometry(0, 125, 86, 25)
        self.buttonZoomOut = QPushButton("-", self)
        self.buttonZoomOut.clicked.connect(self.zoomOut)
        self.buttonZoomOut.setGeometry(86, 125, 86, 25)
        self.buttonRotateLeft = QPushButton("Rotate Window Left", self)
        self.buttonRotateLeft.clicked.connect(self.rotateLeft)
        self.buttonRotateLeft.setGeometry(0, 165, 173, 25)
        self.buttonRotateRight = QPushButton("Rotate Window Right", self)
        self.buttonRotateRight.clicked.connect(self.rotateRight)
        self.buttonRotateRight.setGeometry(0, 190, 173, 25)
        self.buttonPoint = QPushButton("Point", self)
        self.buttonPoint.clicked.connect(self.show_new_window_ponto)
        self.buttonPoint.setGeometry(0, 230, 173, 25)
        self.buttonLine = QPushButton("Line", self)
        self.buttonLine.clicked.connect(self.show_new_window_linha)
        self.buttonLine.setGeometry(0, 255, 173, 25)
        self.buttonPolygon = QPushButton("Wireframe", self)
        self.buttonPolygon.clicked.connect(self.show_new_window_poligono)
        self.buttonPolygon.setGeometry(0, 280, 173, 25)
        self.buttonImport = QPushButton("Import", self)
        self.buttonImport.clicked.connect(self.importObject)
        self.buttonImport.setGeometry(0, 315, 86, 25)

    def show_new_window_ponto(self):
        if self.coordinatesWidgetPonto is None:
            self.coordinatesWidgetPonto = CoordinatesWidgetPonto()
        self.coordinatesWidgetPonto.show()

    def show_new_window_linha(self):
        if self.coordinatesWidgetLinha is None:
            self.coordinatesWidgetLinha = CoordinatesWidgetLinha()
        self.coordinatesWidgetLinha.show()

    def show_new_window_poligono(self):
        if self.coordinatesWidgetPoligono is None:
            self.coordinatesWidgetPoligono = CoordinatesWidgetPoligono()
        self.coordinatesWidgetPoligono.show()

    def rotateRight(self):
        Window.rotateWindow(-10)

    def rotateLeft(self):
        Window.rotateWindow(10)

    def moveUp(self):
        Window.move([0, 5])

    def moveDown(self):
        Window.move([0, -5])

    def moveLeft(self):
        Window.move([-5, 0])

    def moveRight(self):
        Window.move([5, 0])

    def zoomIn(self):
        Window.zoom(0.9)

    def zoomOut(self):
        Window.zoom(1.1)

    def importObject(self):
        (document, filter) = QFileDialog.getOpenFileName(self, 'Open file', './imports', "(*.obj)")
        nameObject = document.split('/')[-1].replace('.obj', '')
        if document == "":
            return
        with open(document) as file:
            data = file.read()
            file_lines = [line.split(" ") for line in data.split("\n")]
            vertices = {}
            faces = []
            for number, line in enumerate(file_lines):
                if line[0] == "v":
                    vertices[number + 1] = (int(line[1]), int(line[2]))
                if line[0] == "f":
                    face = []
                    for index in line[1:]:
                        face.append(vertices[int(index)])
                    faces.append(face)
            points = World.facesToPoints(faces)
            World.addObject(Object(points, nameObject))


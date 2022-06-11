from PyQt5.QtWidgets import QPushButton, QWidget, QFileDialog, QCheckBox, QButtonGroup
from widget.WidgetPonto import CoordinatesWidgetPonto
from widget.WidgetLinha import CoordinatesWidgetLinha
from widget.WidgetWireframe import CoordinatesWidgetPoligono
from widget.WidgetCurve import WidgetCurve
from widget.WidgetSpline import WidgetSpline
from object.window import Window
from object.world import World
from object.object import Object


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.coordinatesWidgetLinha = None
        self.coordinatesWidgetPonto = None  
        self.coordinatesWidgetPoligono = None
        self.coordinatesWidgetCurve = None  
        self.coordinatesWidgetSpline = None  
        self.buttonUp = QPushButton("↑", self)
        self.buttonUp.clicked.connect(self.move_up)
        self.buttonUp.setGeometry(43, 0, 86, 25)
        self.buttonLeft = QPushButton("←", self)
        self.buttonLeft.clicked.connect(self.move_left)
        self.buttonLeft.setGeometry(0, 25, 86, 25)
        self.buttonRight = QPushButton("→", self)
        self.buttonRight.clicked.connect(self.move_right)
        self.buttonRight.setGeometry(86, 25, 86, 25)
        self.buttonDown = QPushButton("↓", self)
        self.buttonDown.clicked.connect(self.move_down)
        self.buttonDown.setGeometry(43, 50, 86, 25)
        self.buttonZoomIn = QPushButton("+", self)
        self.buttonZoomIn.clicked.connect(self.zoom_in)
        self.buttonZoomIn.setGeometry(0, 75, 86, 25)
        self.buttonZoomOut = QPushButton("-", self)
        self.buttonZoomOut.clicked.connect(self.zoom_out)
        self.buttonZoomOut.setGeometry(86, 75, 86, 25)
        self.buttonRotateLeft = QPushButton("Rotacionar Esquerda", self)
        self.buttonRotateLeft.clicked.connect(self.rotate_left)
        self.buttonRotateLeft.setGeometry(0, 165, 173, 25)
        self.buttonRotateRight = QPushButton("Rotacionar Direita", self)
        self.buttonRotateRight.clicked.connect(self.rotate_right)
        self.buttonRotateRight.setGeometry(0, 190, 173, 25)
        self.buttonPoint = QPushButton("Ponto", self)
        self.buttonPoint.clicked.connect(self.show_new_window_ponto)
        self.buttonPoint.setGeometry(0, 160, 173, 25)
        self.buttonLine = QPushButton("Linha", self)
        self.buttonLine.clicked.connect(self.show_new_window_linha)
        self.buttonLine.setGeometry(0, 185, 173, 25)
        self.buttonPolygon = QPushButton("Wireframe", self)
        self.buttonPolygon.clicked.connect(self.show_new_window_poligono)
        self.buttonPolygon.setGeometry(0, 210, 173, 25)
        self.buttonImport = QPushButton("Importar", self)
        self.buttonImport.clicked.connect(self.LerOBJ)
        self.buttonImport.setGeometry(0, 315, 86, 20)
        self.buttonExport = QPushButton("Exportar", self)
        self.buttonExport.clicked.connect(self.DescritorOBJ)
        self.buttonExport.setGeometry(86, 315, 86, 20)
        self.checkBox1 = QCheckBox("Cohen-Sutherland", self)
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda: self.chosen_tecnic(self.checkBox1))
        self.checkBox1.setGeometry(0, 285, 86, 20)
        self.checkBox2 = QCheckBox("Liang-Barsky", self)
        self.checkBox1.stateChanged.connect(lambda: self.chosen_tecnic(self.checkBox2))
        self.checkBox2.setGeometry(86, 285, 86, 20)
        self.buttonCurve = QPushButton("Curva", self)
        self.buttonCurve.clicked.connect(self.show_new_window_curve)
        self.buttonCurve.setGeometry(0, 235, 173, 25)
        self.buttonSpline = QPushButton("Spline", self)
        self.buttonSpline.clicked.connect(self.show_new_window_spline)
        self.buttonSpline.setGeometry(0, 260, 173, 25)
        self.bg = QButtonGroup()
        self.bg.addButton(self.checkBox1, 1)
        self.bg.addButton(self.checkBox2, 2)

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

    def show_new_window_curve(self):
        if self.coordinatesWidgetCurve is None:
            self.coordinatesWidgetCurve = WidgetCurve()
        self.coordinatesWidgetCurve.show()

    def show_new_window_spline(self):
        if self.coordinatesWidgetSpline is None:
            self.coordinatesWidgetSpline = WidgetSpline()
        self.coordinatesWidgetSpline.show()

    def rotate_right(self):
        Window.rotateWindow(-10)

    def rotate_left(self):
        Window.rotateWindow(10)

    def move_up(self):
        Window.move([0, 5])

    def move_down(self):
        Window.move([0, -5])

    def move_left(self):
        Window.move([-5, 0])

    def move_right(self):
        Window.move([5, 0])

    def zoom_in(self):
        Window.zoom(0.9)

    def zoom_out(self):
        Window.zoom(1.1)

    def LerOBJ(self):
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
            points = World.faces_to_points(faces)
            World.add(Object(points, nameObject))

    def DescritorOBJ(self):
        if World.selectedObject is not None:
            (document, filter) = QFileDialog.getSaveFileName(self, 'Save File', './imports', "(*.obj)")
            file = open(document, 'w')
            points = World.selectedObject.points
            text = ''
            faces = 'f'
            for (position, point) in enumerate(points):
                text += 'v ' + str(point.x) + ' ' + str(point.y) + ' 0\n'
                faces += ' ' + str(position + 1)
            text += faces + '\n'
            file.write(text)
            file.close()

    def chosen_tecnic(self, checkBox):
        if checkBox.text() == "Cohen-Sutherland":
            if checkBox.isChecked() == True:
                Window.LINECLIPPING = "CohenSutherland"
        if checkBox.text() == "Liang-Barsky":
            if checkBox.isChecked() == True:
                Window.LINECLIPPING = "LiangBarsky"



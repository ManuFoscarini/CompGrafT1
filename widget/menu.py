from PyQt5.QtWidgets import QPushButton, QWidget, QFileDialog, QCheckBox, QButtonGroup, QLabel, QLineEdit 
from widget.WidgetPonto import CoordinatesWidgetPonto
from widget.WidgetLinha import CoordinatesWidgetLinha
from widget.WidgetWireframe import CoordinatesWidgetPoligono
from widget.coordinatesWidgetObj3D import CoordinatesWidgetObj3D
from widget.WidgetCurve import WidgetCurve
from widget.WidgetSpline import WidgetSpline
from object.window import Window
from object.world import World
from object.object import Object2D


class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.coordinatesWidgetLinha = None
        self.coordinatesWidgetPonto = None  
        self.coordinatesWidgetPoligono = None
        self.coordinatesWidgetCurve = None  
        self.coordinatesWidgetSpline = None
        self.coordinatesWidgetObj3D = None 
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
        self.buttonZoomIn = QPushButton("-", self)
        self.buttonZoomIn.clicked.connect(self.zoom_in)
        self.buttonZoomIn.setGeometry(0, 62, 43, 25)
        self.buttonZoomOut = QPushButton("+", self)
        self.buttonZoomOut.clicked.connect(self.zoom_out)
        self.buttonZoomOut.setGeometry(129, 62, 43, 25)
        self.buttonUp = QPushButton("Up", self)
        self.buttonUp.clicked.connect(self.moveLookUp)
        self.buttonUp.setGeometry(43, 75, 86, 25)
        self.buttonLeft = QPushButton("Look Left", self)
        self.buttonLeft.clicked.connect(self.moveLookLeft)
        self.buttonLeft.setGeometry(0, 100, 86, 25)
        self.buttonRight = QPushButton("Look Right", self)
        self.buttonRight.clicked.connect(self.moveLookRight)
        self.buttonRight.setGeometry(86, 100, 86, 25)
        self.buttonDown = QPushButton("Look Down", self)
        self.buttonDown.clicked.connect(self.moveLookDown)
        self.buttonDown.setGeometry(43, 125, 86, 25)
        self.rotateWinAngLabel = QLabel("Ângulo de rotação:", self)
        self.rotateWinAngLabel.setGeometry(0, 150, 120, 25)
        self.rotateWinAng = QLineEdit("10", self)
        self.rotateWinAng.setGeometry(120, 150, 52, 25)
        self.buttonRotateLeft = QPushButton("Rotacionar", self)
        self.buttonRotateLeft.clicked.connect(self.rotateWindow)
        self.buttonRotateLeft.setGeometry(0, 175, 173, 25)
        self.insertLabel = QLabel("Inserir:", self)
        self.insertLabel.setGeometry(0, 200, 120, 25)
        self.buttonPoint = QPushButton("Ponto", self)
        self.buttonPoint.clicked.connect(self.show_new_window_ponto)
        self.buttonPoint.setGeometry(0, 225, 58, 25)
        self.buttonLine = QPushButton("Linha", self)
        self.buttonLine.clicked.connect(self.show_new_window_linha)
        self.buttonLine.setGeometry(57, 225, 59, 25)
        self.buttonPolygon = QPushButton("WireFrame", self)
        self.buttonPolygon.clicked.connect(self.show_new_window_poligono)
        self.buttonPolygon.setGeometry(115, 225, 57, 25)
        self.buttonSpline = QPushButton("Spline", self)
        self.buttonSpline.clicked.connect(self.show_new_window_spline)
        self.buttonSpline.setGeometry(0, 250, 58, 25)
        self.buttonCurve = QPushButton("Curva", self)
        self.buttonCurve.clicked.connect(self.show_new_window_curve)
        self.buttonCurve.setGeometry(57, 250, 59, 25)
        self.buttonObj3D = QPushButton("Obj 3D", self)
        self.buttonObj3D.clicked.connect(self.show_new_window_obj3d)
        self.buttonObj3D.setGeometry(115, 250, 57, 25)
        self.checkBox1 = QCheckBox("Cohen-Sutherland", self)
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda: self.chosen_tecnic(self.checkBox1))
        self.checkBox1.setGeometry(0, 285, 86, 25)
        self.checkBox2 = QCheckBox("Liang-Barsky", self)
        self.checkBox1.stateChanged.connect(lambda: self.chosen_tecnic(self.checkBox2))
        self.checkBox2.setGeometry(86, 285, 86, 25)
        self.buttonImport = QPushButton("Importar", self)
        self.buttonImport.clicked.connect(self.importObject)
        self.buttonImport.setGeometry(0, 315, 86, 25)
        self.buttonExport = QPushButton("Exportar", self)
        self.buttonExport.clicked.connect(self.exportObject)
        self.buttonExport.setGeometry(86, 315, 86, 25)
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

    def show_new_window_obj3d(self):
        if self.coordinatesWidgetObj3D is None:
            self.coordinatesWidgetObj3D = CoordinatesWidgetObj3D()
        self.coordinatesWidgetObj3D.show()

    def rotateWindow(self):
        angleWin = int(self.rotateWinAng.displayText())
        Window.rotateWindow(angleWin)

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

    def moveLookUp(self):
        Window.move([0, 15])

    def moveLookDown(self):
        Window.move([0, -15])

    def moveLookLeft(self):
        Window.move([-15, 0])

    def moveLookRight(self):
        Window.move([15, 0])

    def chosen_tecnic(self, checkBox):
        if checkBox.text() == "Cohen-Sutherland":
            if checkBox.isChecked() == True:
                Window.LINECLIPPING = "CohenSutherland"
        if checkBox.text() == "Liang-Barsky":
            if checkBox.isChecked() == True:
                Window.LINECLIPPING = "LiangBarsky"

    def importObject(self):
        (document, filter) = QFileDialog.getOpenFileName(self, 'Open file', './object', "(*.obj)")
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
                    vertices[number + 1] = [float(line[1]), float(line[2])]
                if line[0] == "f":
                    face = []
                    for index in line[1:]:
                        face.append(vertices[int(index)])
                    faces.append(face)
            for face in faces:
                World.addObject(Object2D(face, nameObject))

    def exportObject(self):
        if World.selectedObject is not None:
            (document, filter) = QFileDialog.getSaveFileName(self, 'Save File', './object', "(*.obj)")
            if document == "":
                return
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
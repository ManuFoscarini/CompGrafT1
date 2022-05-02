from widget.Widgets import *
from windows.window import Window


class Menu(QWidget):

    def __init__(self):
        super().__init__()
        self.coordinatesWidgetLinha = None 
        self.coordinatesWidgetPonto = None 
        self.coordinatesWidgetPoligono = None  
        self.btn_up = QPushButton("↑", self)
        self.btn_up.clicked.connect(Window.move_up)
        self.btn_up.setGeometry(43, 30, 86, 25)
        self.btn_left = QPushButton("←", self)
        self.btn_left.clicked.connect(Window.move_left)
        self.btn_left.setGeometry(0, 55, 86, 25)
        self.btn_right = QPushButton("→", self)
        self.btn_right.clicked.connect(Window.move_right)
        self.btn_right.setGeometry(86, 55, 86, 25)
        self.btn_down = QPushButton("↓", self)
        self.btn_down.clicked.connect(Window.move_down)
        self.btn_down.setGeometry(43, 80, 86, 25)
        self.btn_inpoint = QPushButton("Point", self)
        self.btn_inpoint.clicked.connect(self.window_ponto)
        self.btn_inpoint.setGeometry(0, 215, 173, 25)
        self.btn_inline = QPushButton("Line", self)
        self.btn_inline.clicked.connect(self.window_linha)
        self.btn_inline.setGeometry(0, 240, 173, 25)
        self.btn_inpol = QPushButton("WireFrame", self)
        self.btn_inpol.clicked.connect(self.window_wireframe)
        self.btn_inpol.setGeometry(0, 265, 173, 25)
        self.btn_zoomin = QPushButton("+", self)
        self.btn_zoomin.clicked.connect(Window.zoom_in)
        self.btn_zoomin.setGeometry(0, 125, 86, 25)
        self.btn_zoomout = QPushButton("-", self)
        self.btn_zoomout.clicked.connect(Window.zoom_out)
        self.btn_zoomout.setGeometry(86, 125, 86, 25)

    def window_ponto(self):
        if self.coordinatesWidgetPonto is None:
            self.coordinatesWidgetPonto = CoordinatesWidgetPonto()
        self.coordinatesWidgetPonto.show()

    def window_linha(self):
        if self.coordinatesWidgetLinha is None:
            self.coordinatesWidgetLinha = CoordinatesWidgetLinha()
        self.coordinatesWidgetLinha.show()

    def window_wireframe(self):
        if self.coordinatesWidgetPoligono is None:
            self.coordinatesWidgetPoligono = CoordinatesWidgetWireframe()
        self.coordinatesWidgetPoligono.show()
from PyQt5.QtWidgets import QMainWindow
from widget.mainWidget import MainWidget
from PyQt5.QtGui import QIcon


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowIcon(QIcon('windows\logo.png'))
        self.setWindowTitle("Computação Gráfica")
        self.setGeometry(200, 200, 1000, 470)
        app_icon = QIcon("windows/logo.png")
        self.setWindowIcon(QIcon(app_icon))
        self.setFixedSize(1000, 470)

        main_widget = MainWidget()
        main_widget.show()

        self.setCentralWidget(main_widget)
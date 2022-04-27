from PyQt5.QtWidgets import QMainWindow
from widget.mainWidget import MainWidget

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Computação Gráfica")
        self.setGeometry(200, 200, 1000, 470)
        self.setFixedSize(1000, 470)
        mainWidget = MainWidget()
        mainWidget.show()
        self.setCentralWidget(mainWidget)

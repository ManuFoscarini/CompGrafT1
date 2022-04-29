from PyQt5.QtWidgets import QMainWindow
from widget.mainWidget import MainWidget
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):   
        self.setWindowIcon(QIcon('windows\logo.png'))    
        self.setWindowTitle("Computação Gráfica")
        self.setGeometry(200, 200, 1000, 470)
        appIcon = QIcon("C:/Users/emanu/Documents/GitHub/CompGrafT1/windows/logo.png")
        self.setWindowIcon(QIcon(appIcon))
        self.setFixedSize(1000, 470)

        mainWidget = MainWidget()
        mainWidget.show()

        self.setCentralWidget(mainWidget)
        

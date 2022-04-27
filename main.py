import sys
from PyQt5.QtWidgets import QApplication
from windows.mainWindow import MainWindow


class Main():
    def __init__(self):
        app = QApplication(sys.argv)
        mainWindow = MainWindow()
        mainWindow.show()

        sys.exit(app.exec_())

Main()

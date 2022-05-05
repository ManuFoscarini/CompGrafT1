
import sys
from PyQt5.QtWidgets import QApplication
from windows.mainWindow import MainWindow


class Main:
    
    def __init__(self):
        app = QApplication(sys.argv)
        mw = MainWindow()
        mw.show()

        sys.exit(app.exec_())


if __name__ == '__main__':
    Main()

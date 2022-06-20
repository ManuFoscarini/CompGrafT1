
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


# TODO: Fiz toda a implementação da a parte da inserção 3D mas está dando erro, se puder dar uma conferida para ganharmos alguma porcentagem da nota.
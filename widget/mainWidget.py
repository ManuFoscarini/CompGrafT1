from PyQt5.QtWidgets import QGridLayout, QWidget

from widget.menu import Menu
from widget.viewport import ViewPort
from widget.objectsList import ObjectsList


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        menu = Menu()

        viewPort = ViewPort()

        objectsList = ObjectsList()

        grid = QGridLayout()
        grid.setSpacing(0)

        grid.addWidget(menu, 0, 0)
        grid.addWidget(objectsList, 1, 0)
        grid.addWidget(viewPort, 0, 1)
        self.setLayout(grid)

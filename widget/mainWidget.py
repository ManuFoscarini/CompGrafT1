from PyQt5.QtWidgets import QGridLayout, QWidget

from widget.Menu import Menu
from widget.view import ViewPort
from widget.objectsList import ObjectsList


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        leftWidget = Menu()

        rightWidget = ViewPort()

        objectsList = ObjectsList()

        grid = QGridLayout()
        grid.setSpacing(0)

        grid.addWidget(leftWidget, 0, 0)
        grid.addWidget(objectsList, 1, 0)
        grid.addWidget(rightWidget, 0, 1)

        self.setLayout(grid)

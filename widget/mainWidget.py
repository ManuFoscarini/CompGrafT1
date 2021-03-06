from PyQt5.QtWidgets import QGridLayout, QWidget

from widget.Menu import Menu
from widget.view import ViewPort
from widget.objectsList import ObjectsList


class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        menu = Menu()

        view_port = ViewPort()

        objects_list = ObjectsList()

        grid = QGridLayout()
        grid.setSpacing(0)

        grid.addWidget(menu, 0, 0)
        grid.addWidget(objects_list, 1, 0)
        grid.addWidget(view_port, 0, 1)

        self.setLayout(grid)

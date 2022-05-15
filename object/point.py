from PyQt5.QtCore import QPoint

class Point(QPoint):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

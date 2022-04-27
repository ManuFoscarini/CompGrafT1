class Window():
    xmin = 0
    xmax = 800
    ymin = 0
    ymax = 450

    @staticmethod
    def moveLeft():
        Window.xmin -= 5
        Window.xmax -= 5

    @staticmethod
    def moveRight():
        Window.xmin += 5
        Window.xmax += 5

    @staticmethod
    def moveDown():
        Window.ymin -= 5
        Window.ymax -= 5

    @staticmethod
    def moveUp():
        Window.ymin += 5
        Window.ymax += 5

    @staticmethod
    def zoomIn():
        if ((Window.ymax > (Window.ymin + 50)) and (Window.xmax > (Window.xmin + 50))):
            Window.ymin += 5
            Window.ymax -= 5
            Window.xmin += 5
            Window.xmax -= 5

    @staticmethod
    def zoomOut():
        Window.ymin -= 5
        Window.ymax += 5
        Window.xmin -= 5
        Window.xmax += 5

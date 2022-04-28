class Window():
    xmin = 0
    xmax = 800
    ymin = 0
    ymax = 450

    def moveLeft():
        Window.xmin -= 10
        Window.xmax -= 10

    def moveRight():
        Window.xmin += 10
        Window.xmax += 10

    def moveDown():
        Window.ymin -= 10
        Window.ymax -= 10

    def moveUp():
        Window.ymin += 10
        Window.ymax += 10

    def zoomIn():
        if ((Window.ymax > (Window.ymin + 100)) and (Window.xmax > (Window.xmin + 50))):
            Window.ymin += 10
            Window.ymax -= 10
            Window.xmin += 10
            Window.xmax -= 10
    def zoomOut():
        Window.ymin -= 10
        Window.ymax += 10
        Window.xmin -= 10
        Window.xmax += 10

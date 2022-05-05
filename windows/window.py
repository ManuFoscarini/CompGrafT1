from widget.viewport import ViewPort as vp


class Window:
    x_min = 0
    x_max = 800
    y_min = 0
    y_max = 450

    @staticmethod
    def move_left():
        Window.x_min -= 10
        Window.x_max -= 10
        vp.YAxis.x1 += 10
        vp.YAxis.x2 += 10

    @staticmethod
    def move_right():
        Window.x_min += 10
        Window.x_max += 10
        vp.YAxis.x1 -= 10
        vp.YAxis.x2 -= 10

    @staticmethod
    def move_down():
        Window.y_min -= 10
        Window.y_max -= 10
        vp.XAxis.y1 -= 10
        vp.XAxis.y2 -= 10

    @staticmethod
    def move_up():
        Window.y_min += 10
        Window.y_max += 10
        vp.XAxis.y1 += 10
        vp.XAxis.y2 += 10

    @staticmethod
    def zoom_in():
        if (Window.y_max > (Window.y_min + 100)) and (Window.x_max > Window.x_min + 50):
            Window.y_min += 10
            Window.y_max -= 10
            Window.x_min += 10
            Window.x_max -= 10

    @staticmethod
    def zoom_out():
        Window.y_min -= 10
        Window.y_max += 10
        Window.x_min -= 10
        Window.x_max += 10
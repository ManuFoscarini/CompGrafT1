from windows.configs import Configs
from windows.window import Window


class TransformPoint:

    @staticmethod
    def viewport_transformation(point):
        x = ((point.x - Window.x_min) / (Window.x_max - Window.x_min)) * \
            (Configs.x_max - Configs.x_min)
        y = (1 - ((point.y - Window.y_min) / (Window.y_max - Window.y_min))
             ) * (Configs.y_max - Configs.y_min)
        return x, y
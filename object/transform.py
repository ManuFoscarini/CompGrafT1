from windows.configs import Configs
from windows.window import Window


class transform_point:
    def transformViewport(self, point):
        x = ((point.x - Window.xmin) / (Window.xmax - Window.xmin)) * \
            (Configs.xmax - Configs.xmin)
        y = (1 - ((point.y - Window.ymin) / (Window.ymax - Window.ymin))
             ) * (Configs.ymax - Configs.ymin)
        return (x, y)

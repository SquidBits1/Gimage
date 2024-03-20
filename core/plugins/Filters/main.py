"""
Filters\main.py -
The plugin classes are contained here.
"""

from core.plugin_manager.plugin_manager import AbstractPlugin
from .general_filter import rgb_factors, conv_to_gs
from .filters import sepia_filter, red_filter, green_filter, blue_filter


class Sepia(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def edit_function(self, image):
        return rgb_factors(image, sepia_filter)


class Red(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def edit_function(self, image):
        return rgb_factors(image, red_filter)


class Green(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def edit_function(self, image):
        return rgb_factors(image, green_filter)


class Blue(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def edit_function(self, image):
        return rgb_factors(image, blue_filter)


class Greyscale(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def edit_function(self, image):
        return conv_to_gs(image)

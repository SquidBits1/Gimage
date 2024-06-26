"""
pixel_sorting\main.py -
The plugins classes are contained here.
"""

from core.plugin_manager.plugin_manager import AbstractPlugin
from .pixel_sort import pixelsort
from core.GUI.widgets.options import ComboBoxOptions


class PixelSort(AbstractPlugin):

    def __init__(self):
        super().__init__()
        # Potential options are right, down, left and up
        self.rotation_dict = {"right": 0, "down": 1, "left": 2, "up": 3}

    def create_option(self):
        self.option_widget = ComboBoxOptions(self.rotation_dict.keys())

    def edit_function(self, image, rotation):
        return pixelsort(image, self.rotation_dict[rotation])

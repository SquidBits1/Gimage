from core.plugin_manager.plugin_manager import ImagePlugin
from .pixel_sort import pixelsort
from core.GUI.Widgets.options import ComboBoxOptions


class PixelSort(ImagePlugin):

    def __init__(self):
        super().__init__()
        self.rotation_dict = {"right": 0, "down": 1, "left": 2, "up": 3}

    def create_option(self):
        self.option_widget = ComboBoxOptions(self.rotation_dict.keys())

    def plugin_function(self, image, rotation):
        return pixelsort(image, self.rotation_dict[rotation])

from core.plugin_manager.plugin_manager import AbstractPlugin
from core.GUI.Widgets.options import ComboBoxOptions
from .transform import rotate, flip


class Rotate(AbstractPlugin):

    def __init__(self):
        super().__init__()
        self.rotation_dict = {"90": 1, "180": 2, "270": 3}

    def create_option(self):
        self.option_widget = ComboBoxOptions(self.rotation_dict.keys())

    def plugin_function(self, image, rotation):
        return rotate(image, self.rotation_dict[rotation])


class Flip(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image):
        return flip(image)

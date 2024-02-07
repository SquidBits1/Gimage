from .simple_threshold import binary_threshold, halloween, glitch
from core.plugin_manager.plugin_manager import ImagePlugin
from core.GUI.Widgets.options import SliderOptions


class SimpleThreshold(ImagePlugin):

    def __init__(self):
        super().__init__()

    def create_option(self):
        self.option_widget = SliderOptions(0, 255, 127)

    def plugin_function(self, image, threshold):
        return binary_threshold(image, threshold)


class Halloween(ImagePlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, *args):
        return halloween(image)


class Glitch(ImagePlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, *args):
        return glitch(image)

from .simple_threshold import binary_threshold, halloween, glitch
from core.plugin_manager.plugin_manager import ImagePlugin
from core.GUI.Widgets.configurers import SliderOptions, Options


class SimpleThreshold(ImagePlugin):

    def __init__(self):
        super().__init__()

    def create_option(self):
        self.option_widget = SliderOptions(self)
        return self.option_widget

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

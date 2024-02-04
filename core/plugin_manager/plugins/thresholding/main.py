from .simple_threshold import binary_threshold, halloween, glitch
from core.plugin_manager.plugin_manager import ImagePlugin


class SimpleThreshold(ImagePlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, **args):
        return binary_threshold(image)


class Halloween(ImagePlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, **args):
        return halloween(image)


class Glitch(ImagePlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, **args):
        return glitch(image)

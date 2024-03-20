"""
thresholding\main.py -
The plugins classes are contained here.
"""

from .simple_threshold import binary_threshold, deepfry, deepfry_truncate, threshold_to_zero
from core.plugin_manager.plugin_manager import AbstractPlugin
from core.GUI.widgets.options import SliderOptions


class SimpleThreshold(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def create_option(self):
        self.option_widget = SliderOptions(0, 255, 127)

    def edit_function(self, image, threshold):
        return binary_threshold(image, threshold)


class Deepfry(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def create_option(self):
        self.option_widget = SliderOptions(0, 255, 127)

    def edit_function(self, image, threshold):
        return deepfry(image, threshold)


class DeepfryTruncate(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def create_option(self):
        self.option_widget = SliderOptions(0, 255, 127)

    def edit_function(self, image, threshold):
        return deepfry_truncate(image, threshold)


class ThreshholdToZero(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def create_option(self):
        self.option_widget = SliderOptions(0, 255, 127)

    def edit_function(self, image, threshold):
        return threshold_to_zero(image, threshold)

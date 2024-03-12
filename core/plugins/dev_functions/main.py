from core.plugin_manager.plugin_manager import AbstractPlugin
from copy import copy
from core.GUI.widgets.options import Options, SliderOptions, ComboBoxOptions


class Copy(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, *args):
        return copy(image)

    def create_option(self):
        options = ["Test1: ATTENTION THIS IS A TEST LOL", "This is also a test"]
        self.option_widget = ComboBoxOptions(options)


class Test(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, *args):
        self.state = "This is a test hopefully this works"

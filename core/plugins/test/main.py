from core.plugin_manager.plugin_manager import AbstractPlugin
from core.GUI.widgets.options import ComboBoxOptions


class Test(AbstractPlugin):

    def __init__(self):
        super().__init__()

    def edit_function(self, image, *args):
        return image.copy()

    def create_option(self):
        options = ["Test_option1", "Test_option2"]
        self.option_widget = ComboBoxOptions(options)

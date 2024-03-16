from core.GUI.widgets.options import Options
from .util.image_data import ImageData


class PluginRegistry(type):
    plugins = []

    def __init__(cls, name, bases, attr):
        if name != "AbstractPlugin":
            PluginRegistry.plugins.append(cls)


class AbstractPlugin(metaclass=PluginRegistry):
    def __init__(self):
        self.parent = None
        self.image_data: None | ImageData = None
        self.image = None
        self.state: str = ""
        self.option_widget: None | Options = None

    def plugin_function(self, *args):
        return None

    def get_data(self):
        # gets the data from the options bar
        data = self.option_widget.get_value()
        # uses this to perform the edit
        if data:
            self.process(data)
        else:
            self.process()

    def create_option(self):
        self.option_widget = Options()

    def invoke(self):
        """
        Starts the plugin flow:
        :param kwargs: possible arguments used
        :return: a fully processed image
        """
        self.parent.clear_option()
        # gives the plugin access to the image data class
        self.image_data: ImageData = self.parent.image_data

        if not self.image_data:
            self.state = "No image to edit :("
            return False

        # Creates an Options bar widget
        self.create_option()
        # Adds the widget to the Main window
        self.parent.add_options(self.option_widget)
        # Connects the button press to getting the data from the options bar
        self.option_widget.connect(self.get_data)

    def process(self, *args):
        self.image = self.image_data.processed_image_data[-1]
        self.parent.current_function = self
        self.image_data.add_image(self.plugin_function(self.image, *args))
        self.parent.process_image()
        self.option_widget.deleteLater()

    # Uses repr to represent the current state of the Plugin
    def __repr__(self):
        return self.state

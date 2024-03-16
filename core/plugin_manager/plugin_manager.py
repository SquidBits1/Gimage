from core.GUI.widgets.options import Options
from .util.image_data import ImageData


class PluginRegistry(type):
    """
    This is a metaclass that changes the functionality of classes that use it.
    If a class has PluginRegistry as its metaclass, when it is created (the class NOT an instance of it), a reference to
    the class is added to the plugins list.
    """
    plugins = []

    def __init__(cls, name, bases, attr):
        if name != "AbstractPlugin":
            PluginRegistry.plugins.append(cls)


class AbstractPlugin(metaclass=PluginRegistry):
    """
    Defines an abstract plugin that all plugins must subclass from.
    """
    def __init__(self):
        # This will be the reference to the "parent class". In my program this will be MainWindow.
        self.parent = None
        # Plugins will have access to the ImageData class of the image they are editing
        self.image_data: None | ImageData = None
        self.image = None
        self.state: str = ""
        self.option_widget: None | Options = None

    def edit_function(self, *args):
        """
        This is the function that actually changes image data
        :param args: args contains the different arguments of this function.
         Almost all plugins will take image data as an argument.
         Other examples of arguments are rotation, threshold value etc.
        :return:
        """
        return None

    def get_data(self):
        """
        Gets data from the options bar.
        :return:
        """
        # gets the data from the options bar
        data = self.option_widget.get_value()
        # uses this to perform the edit
        if data is not None:
            self.edit_image(data)
        else:
            self.edit_image()

    def create_option(self):
        self.option_widget = Options()

    def invoke(self):
        """
        Starts the plugin flow:
        :return: False if no image data
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

    def edit_image(self, *args):
        """
        Performs edit on image and then shows it on window
        :param args: All arguments needed to be passed to the edit function.
        :return:
        """
        # Gets image to edit
        self.image = self.image_data.processed_image_data[-1]
        self.parent.current_function = self
        # Performs plugin function
        self.image_data.add_image(self.edit_function(self.image, *args))
        # shows image on window
        self.parent.process_image()
        self.option_widget.deleteLater()

    def __repr__(self):
        return self.state

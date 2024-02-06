from core.GUI.Widgets.configurers import Options


class PluginRegistry(type):
    plugins = []

    def __init__(cls, name, bases, attr):
        if name != "ImagePlugin":
            PluginRegistry.plugins.append(cls)


class ImagePlugin(metaclass=PluginRegistry):
    def __init__(self):
        self.parent = None
        self.image = None
        self.state: str = ""
        self.option_widget = None

    def plugin_function(self, *args):
        return None

    def create_option(self):
        self.option_widget = Options(self)
        return self.option_widget

    def invoke(self, **kwargs):
        """
        Starts the plugin flow:
        :param kwargs: possible arguments used
        :return: a fully processed image
        """
        self.create_option()
        self.parent.add_options(self.option_widget)


    def process(self, *args):
        self.image = self.parent.get_current_image()
        self.parent.current_function = self
        try:
            self.parent.add_image(self.plugin_function(self.image, *args))
        except ValueError as error:
            self.state = f"Textbox changed: ERROR {error}"
        self.parent.process_image()
        self.option_widget.deleteLater()

    # Uses repr to represent the current state of the Plugin
    def __repr__(self):
        return self.state

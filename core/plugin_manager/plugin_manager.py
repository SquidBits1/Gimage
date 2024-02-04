class PluginRegistry(type):
    plugins = []

    def __init__(cls, name, bases, attr):
        if name != "ImagePlugin":
            PluginRegistry.plugins.append(cls)


class ImagePlugin(metaclass=PluginRegistry):
    def __init__(self):
        self.parent = None
        self.image = None
        self.kwargs = {}
        self.state: str = ""

    def plugin_function(self, image, **args):
        return None

    def invoke(self, **kwargs):
        """
        Starts the plugin flow:
        :param kwargs: possible arguments used
        :return: a fully processed image
        """
        self.image = self.parent.get_current_image()
        self.parent.current_function = self
        try:
            self.parent.add_image(self.plugin_function(self.image, **self.kwargs))
        except ValueError as error:
            self.state = f"Textbox changed: ERROR {error}"
        self.parent.process_image()

    # Uses repr to represent the current state of the Plugin
    def __repr__(self):
        return self.state

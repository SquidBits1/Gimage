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

    def plugin_function(self, image, **args):
        return None

    def invoke(self, parent, **kwargs):
        """
        Starts the plugin flow:
        :param image: the image data used
        :param kwargs: possible arguments used
        :return: a fully processed image
        """
        self.image = parent.get_current_image()
        self.parent.current_function = None
        try:
            self.parent.add_image(self.plugin_function(self.image, **self.kwargs))
        except ValueError as error:
            print(f"Textbox changed: ERROR {error}")
        self.parent.process_image()

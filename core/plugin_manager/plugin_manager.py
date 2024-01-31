class PluginRegistry(type):
    plugins = []

    def __init__(cls, name, bases, attr):
        if name != "ImagePlugin":
            PluginRegistry.plugins.append(cls)


class ImagePlugin(metaclass=PluginRegistry):
    def __init__(self):
        ...

    def invoke(self, image, **kwargs):
        """
        Starts the plugin flow:
        :param image: the image data used
        :param kwargs: possible arguments used
        :return: a fully processed image
        """
        pass

    def get_name(self):
        return
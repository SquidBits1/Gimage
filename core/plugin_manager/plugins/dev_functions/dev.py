from core.plugin_manager.plugin_manager import ImagePlugin
from copy import copy


class Copy(ImagePlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, **args):
        return copy(image)


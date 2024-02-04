from core.plugin_manager.plugin_manager import ImagePlugin
from .pixel_sort import pixelsort

class PixelSort(ImagePlugin):

    def __init__(self):
        super().__init__()

    def plugin_function(self, image, **args):
        return pixelsort(image)
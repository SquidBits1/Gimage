from dataclasses import dataclass
from core.plugin_manager.imageplugin import ImagePlugin


@dataclass
class ImagePlugin:

    @staticmethod
    def copy(image):
        return image.copy()

    @staticmethod
    def test(image):
        return image
from dataclasses import dataclass
from core.plugin_manager.imageplugin import ImagePlugin


@dataclass
class ImagePlugin:

    def copy(self, image):
        return image.copy()

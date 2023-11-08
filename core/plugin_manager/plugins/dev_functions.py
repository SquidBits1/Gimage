from dataclasses import dataclass


@dataclass
class ImagePlugin:

    @staticmethod
    def copy(image):
        return image.copy()

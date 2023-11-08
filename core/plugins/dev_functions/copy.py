from dataclasses import dataclass
from core.plugins import factory


@dataclass
class DevPlugin:

    def copy(image):
        return image


def register() -> None:
    factory.register('DevPlugin', DevPlugin)

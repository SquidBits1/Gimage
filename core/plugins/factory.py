from typing import Any, Callable
from core.plugins.image_plugin import ImagePlugin

plugin_creation_funcs: dict[str, Callable[..., ImagePlugin]] = {}


def register(image_plugin_name: str, creator_fn: Callable[..., ImagePlugin]) -> None:
    plugin_creation_funcs[image_plugin_name] = creator_fn


def unregister(image_plugin_name: str):
    plugin_creation_funcs.pop(image_plugin_name, None)


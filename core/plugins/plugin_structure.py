from typing import Callable
import importlib

import numpy as np


class PluginInterface:

    @staticmethod
    def register() -> None:
        """Every plugin has one method (in the file it will be a function) called register. It should register in a
        factory."""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialise()

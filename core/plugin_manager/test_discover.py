from . import discover
from core.plugin_manager.plugin_manager import AbstractPlugin

plugins = discover.setup_configuration(discover.discover_plugins())


def test_discover_plugins():
    names = plugins.keys()
    assert list(names) == ["Filters", "Pixel Sorting", "Thresholding", "Transform"]


def test_register_plugins():
    classes = []
    values = plugins.values()
    for package in values:
        for plugin in package:
            classes.append(plugin)
    is_plugin = [True if issubclass(i, AbstractPlugin) else False for i in classes]
    assert all(is_plugin)

import os
import yaml
from core.plugin_manager.util.models import PluginConfig
from dacite import from_dict
from importlib import import_module
from core.plugin_manager.plugin_manager import PluginRegistry


def discover_plugins():
    """
    Discovers plugin packages in the plugin directory
    :return: an iterator that contains every plugin package
    """
    path = os.path.abspath(os.path.dirname(__file__))

    return os.scandir(os.path.join(path, r"..\plugins"))


def setup_configuration(dirs: iter):
    """
    Sets up the plugins by dynamically importing its main file
    :param dirs: an iterable of package directories
    :return: A dictionary containing plugins of the form [plugin name: plugin class]
    """
    plugins = {}
    for plugin_dir in dirs:
        # Gets plugin config
        config: PluginConfig = read_configuration(plugin_dir)
        if config:
            # the plugin file to be run. This contains the plugin classes
            plugin_main = config.runtime.main
            module_target = f'{convert_to_import(plugin_dir.path)}.{plugin_main}'
            import_module(module_target)
            # Gets access to the plugin classes that have just been registered using the PluginRegistry
            current_dir_plugins = PluginRegistry.plugins.copy()
            PluginRegistry.plugins.clear()
            # Adds plugins to a plugin dictionary
            plugins[config.name] = current_dir_plugins

    return plugins


def read_configuration(dir: str):
    """
    Reads the config file of a plugin package and turns it into a data class
    :param dir: The directory containing a plugin.yaml file
    :return: An instance of a PluginConfig data class
    """
    plugin_path = os.path.join(dir, "plugin.yaml")
    # Checks if a config file exists for the files in the directory
    if not os.path.exists(plugin_path):
        return False
    data = None
    try:
        with open(plugin_path) as file:
            data = yaml.safe_load(file)
    except FileNotFoundError as e:
        print(f"Could not find configuration file {e}")

    # converts config file into a python data class
    plugin_config = from_dict(data_class=PluginConfig, data=data)
    return plugin_config


def convert_to_import(path):
    """
    Converts a path into the correct format for importing
    :param path: path to be formatted
    :return: correctly formatted path
    """
    normalised = os.path.normpath(path)
    a = normalised.split("\\")
    core_index = a.index("core")
    return ".".join(a[core_index:])

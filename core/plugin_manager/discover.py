import os
import yaml
from core.plugin_manager.util.models import PluginConfig
from dacite import from_dict
from importlib import import_module
from core.plugin_manager.plugin_manager import PluginRegistry


def discover_plugins():
    path = os.path.abspath(os.path.dirname(__file__))

    return os.scandir(os.path.join(path, r"plugins"))


def setup_configuration(dirs: iter):
    # TODO make it so that the configs variable contains the plugin class and its config
    plugins = {}
    for plugin_dir in dirs:
        config = read_configuration(plugin_dir)
        if config:
            plugin_main = config.runtime.main
            module_target = f'{convert_to_import(plugin_dir.path)}.{plugin_main}'
            module = import_module(module_target)
            current_dir_plugins = PluginRegistry.plugins.copy()
            PluginRegistry.plugins.clear()
            plugins[config.name] = current_dir_plugins

        else:
            pass
            # print(f"No config for directory {plugin_dir.name}")
    return plugins

def read_configuration(dir: str):
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

    # loads in a plugin
    plugin_config = from_dict(data_class=PluginConfig, data=data)
    return plugin_config


def convert_to_import(path):
    a = path.split("\\")
    core_index = a.index("core")
    return (".").join(a[core_index:])

#
# a = setup_configuration(discover_plugins())
# print(a)

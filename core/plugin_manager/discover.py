import os
import yaml
from core.plugin_manager.util.models import PluginConfig
from dacite import from_dict
from importlib import import_module


class PluginUtil:

    @staticmethod
    def discover_plugins():
        path = os.path.abspath(os.path.dirname(__file__))

        return os.path.join(path, r"plugins")

    def setup_configuration(self, dirs: list[str]):
        for plugin_dir in dirs:
            config = self.__read_configuration(plugin_dir)
            plugin_main = config.runtime.main
            module_target = f'{plugin_dir}.{plugin_main}'
            module = import_module(module_target)



    @staticmethod
    def __read_configuration(dir: str):
        data = None
        try:
            with open(os.path.join(dir, "plugin.yaml")) as file:
                data = yaml.safe_load(file)
        except FileNotFoundError as e:
            print(f"Could not find configuration file {e}")

        plugin_config = from_dict(data_class=PluginConfig, data=data)
        return plugin_config


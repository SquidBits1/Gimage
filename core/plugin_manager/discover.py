import os
import yaml
from core.plugin_manager.util.models import PluginConfig
from dacite import from_dict
from importlib import import_module

class PluginUtil:

    @staticmethod
    def discover_plugins():
        path = os.path.abspath(os.path.dirname(__file__))

        return os.scandir(os.path.join(path, r"plugins"))

    @staticmethod
    def setup_configuration(dirs: iter):
        for plugin_dir in dirs:
            config = PluginUtil.read_configuration(plugin_dir)
            if config:
                plugin_main = config.runtime.main
                module_target = f'{plugin_dir.path}.{plugin_main}'
                print(module_target)
                module = import_module(module_target)
            else:
                print("No config")

    @staticmethod
    def read_configuration(dir: str):
        plugin_path = os.path.join(dir, "plugin.yaml")
        print(plugin_path)
        if not os.path.exists(plugin_path):
            return False
        data = None
        try:
            with open(plugin_path) as file:
                data = yaml.safe_load(file)
        except FileNotFoundError as e:
            print(f"Could not find configuration file {e}")

        plugin_config = from_dict(data_class=PluginConfig, data=data)
        return plugin_config

    @staticmethod
    def convert_to_import(path="C:\\Users\gilsmi0809\PycharmProjects\Gimage\core\plugin_manager\plugins\dev_functions"):
        a = path.split("\\")
        print(a)
        core_index = a.index("core")
        return ("\\").join(a[:core_index]) + "\\" + (".").join(a[core_index:])



# PluginUtil.setup_configuration(PluginUtil.discover_plugins())


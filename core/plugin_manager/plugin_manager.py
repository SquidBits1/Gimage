import importlib.util
import inspect
import os
from core.plugin_manager.imageplugin import ImagePlugin


class PluginManager(ImagePlugin):

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.plugins = dict()
        self.method_list = {}

    # loads plugins using path specified for PluginManager
    def load_plugins(self):
        for entry in os.listdir(self.folder_path):
            # Path to each item in directory
            entry_path = os.path.join(self.folder_path, entry)
            if entry.startswith('__'):
                pass
            # if item is directory, initialises new PluginManager for that plugin package, and appends that object to
            # self.plugins | Then loads plugins into that PluginManager
            elif os.path.isdir(entry_path):
                self.plugins[entry] = PluginManager(entry_path)
                self.plugins[entry].load_plugins()
            elif entry.endswith('.py'):
                self.load_plugin_from_file(entry_path)

        self.load_methods()

    def load_plugin_from_file(self, path):
        plugin_name = os.path.basename(path).split('.')[0]
        spec = importlib.util.spec_from_file_location(plugin_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, 'ImagePlugin'):
            plugin_instance = module.ImagePlugin()
            self.plugins[plugin_name] = plugin_instance
            print(f'Loaded Plugin: {plugin_name}')
            print('---------------')

    def load_methods(self):
        for plugin_name, plugin_instance in self.plugins.items():
            if isinstance(plugin_instance, PluginManager):
                plugin_instance.load_methods()
            else:
                base_class_methods = dir(ImagePlugin())
                all_class_methods = dir(plugin_instance)
                methods = dict()
                # makes a dictionary of methods with method names if method has valid signature
                for method in all_class_methods:
                    method_instance = getattr(plugin_instance, method)
                    if method not in base_class_methods and 'image' in inspect.signature(method_instance).parameters:
                        methods[method] = method_instance
                self.method_list[plugin_name] = methods

    def get_sub_plugins(self):
        return {name: plugin for name, plugin in self.plugins.items() if isinstance(plugin, PluginManager)}

    def get_plugins(self):
        return {name: plugin for name, plugin in self.plugins.items() if not isinstance(plugin, PluginManager)}

    def get_methods(self):
        methods = [method for method in self.method_list.values()]
        return methods


if __name__ == '__main__':
    plugins = PluginManager('C:\\Users\\Gilad\\PycharmProjects\\Gilad-Gimp\\core\\plugin_manager\\plugins')
    plugins.load_plugins()
    print(plugins.get_plugins())

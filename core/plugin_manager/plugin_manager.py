import importlib.util
import os


class PluginManager:

    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.plugins = dict()
        self.method_list = {}
        self.has_plugin = False

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

        self.get_methods()

    def load_plugin_from_file(self, path):
        plugin_name = os.path.basename(path).split('.')[0]
        spec = importlib.util.spec_from_file_location(plugin_name, path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)

        if hasattr(module, 'ImagePlugin'):
            plugin_instance = module.ImagePlugin()
            self.plugins[plugin_name] = plugin_instance
            print(f'Loaded Plugin: {plugin_name}')
            self.has_plugin = True
            print('---------------')

    def get_methods(self):
        for item in self.plugins:
            if type(item) == PluginManager:
                item.get_methods()
            else:
                item_list = [func for func in dir(item) if not func.startswith('__')]
                self.method_list[item] = item_list


if __name__ == '__main__':
    plugins = PluginManager('C:\\Users\\Gilad\\PycharmProjects\\Gilad-Gimp\\core\\plugin_manager\\plugins')
    plugins.load_plugins()

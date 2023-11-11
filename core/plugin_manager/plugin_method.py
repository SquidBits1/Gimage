import inspect


# constructs a plugin class for a method
class PluginMethod:

    def __init__(self, method):
        self.method = method
        self.signature = inspect.signature(self.method)
        self.argument_dict = {}
        self.parent = None
        self.textbox = self.method.__name__

        for argument in self.signature.parameters:
            self.argument_dict[argument] = self.signature.parameters[argument].default

        self.image_data = self.argument_dict.pop('image')

    def run_function(self):
        self.image_data = self.parent.image.processed_image_data[-1].copy()
        if self.image_data is None:
            self.parent.current_function = None
            return
        self.parent.current_function = self
        try:
            self.parent.image.add_image(self.method(self.image_data, *self.argument_dict.values()))
        except ValueError as error:
            print('textbox changed')
            self.textbox = f"ERROR: {error}"
        self.parent.process_image()

    def __repr__(self):
        return self.textbox

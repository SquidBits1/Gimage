import inspect


# constructs a plugin class for a method
class Factory:

    def __init__(self, method):
        self.method = method
        self.signature = inspect.signature(self.method)
        self.argument_dict = {}
        self.parent = None

        for argument in self.signature.parameters:
            self.argument_dict[argument] = self.signature.parameters[argument].default

        self.image_data = self.argument_dict.pop('image')

    def run_function(self):
        self.image_data = self.parent.image.source_image_data
        if self.image_data is None:
            self.parent.current_function = None
            return
        self.parent.current_function = repr(self)
        try:
            self.parent.image.add_image(self.method(self.image_data, *self.argument_dict.values()))
        except Exception as error:
            print(f'ERROR: {error}')
            print(f'{self.argument_dict}')

        self.parent.process_image()



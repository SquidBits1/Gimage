from Thresholding import simple_threshold


class Plugin:

    def __init__(self, function):
        self.image_data = None
        self.function = function
        self.parent = None

    def run_function(self):
        self.parent.current_function = self
        self.image_data = self.parent.source_image_data
        self.parent.processed_source_image_data = self.function(self.image_data)
        self.parent.process_image()

    def process(self):



class ThresholdingPlugin(Plugin):

    def __init__(self, function):
        super().__init__(function)
        self.threshold = 95

    def run_function(self):
        self.parent.current_function = self
        self.image_data = self.parent.source_image_data
        self.parent.processed_source_image_data = self.function(self.image_data, self.threshold)
        self.parent.process_image()


plugins = {
    'binary threshold': ThresholdingPlugin(simple_threshold.binary_threshold)
}

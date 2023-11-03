from Thresholding import simple_threshold
from Pixel_Sorting import body


class Plugin:

    def __init__(self, function):
        self.image_data = None
        self.function = function
        self.parent = None

    def run_function(self):
        self.parent.current_function = self
        self.image_data = self.parent.source_image_data
        self.function_input()
        self.parent.process_image()

    def data_check(self):
        if not self.image_data:
            return True
        else:
            return False

    def function_input(self):
        self.parent.processed_source_image_data = self.function(self.image_data)


class ThresholdingPlugin(Plugin):

    def __init__(self, function):
        super().__init__(function)
        self.threshold = 95

    def function_input(self):
        self.parent.processed_source_image_data = self.function(self.image_data, self.threshold)


class PixelSortPlugin(Plugin):

    def __init__(self, function):
        super().__init__(function)
        self.rotation = 1
        self.sorting_func = body.sorting_functions.luminance

    def function_input(self):
        self.parent.processed_source_image_data = self.function(self.image_data, self.rotation, self.sorting_func)


plugins = {
    'binary threshold': ThresholdingPlugin(simple_threshold.binary_threshold),
    'inverse binary threshold': ThresholdingPlugin(simple_threshold.inverse_binary_threshold),
    'halloween (experimental scary ahh)': ThresholdingPlugin(simple_threshold.halloween),
    'truncate threshold': ThresholdingPlugin(simple_threshold.truncate_threshold),
    'threshold to zero': ThresholdingPlugin(simple_threshold.threshold_to_zero),
    'pixel sort': PixelSortPlugin(body.pixelsort)

}

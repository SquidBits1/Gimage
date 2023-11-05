from ..Thresholding import simple_threshold
from ..Pixel_Sorting import body
from ..Dev_Functions import copy


class Plugin:

    def __init__(self, function, name):
        self.name = name
        self.image_data = None
        self.function = function
        self.parent = None

    def run_function(self):

        self.image_data = self.parent.image.source_image_data
        # checks to see if image is loaded
        if self.image_data is None:
            self.parent.current_function = None
            return
        self.parent.current_function = repr(self)
        self.function_input()
        self.parent.process_image()

    def data_check(self):
        if not self.image_data:
            return True
        else:
            return False

    def function_input(self):
        self.parent.image.add_image(self.function(self.image_data))

    def __repr__(self):
        return self.name


class ThresholdingPlugin(Plugin):

    def __init__(self, function, name):
        super().__init__(function, name)
        self.threshold = 95

    def function_input(self):
        self.parent.image.add_image(self.function(self.image_data, self.threshold))


class PixelSortPlugin(Plugin):

    def __init__(self, function, name):
        super().__init__(function, name)
        self.rotation = 1
        self.sorting_func = body.sorting_functions.luminance

    def function_input(self):
        self.parent.image.add_image(self.function(self.image_data, self.rotation, self.sorting_func))


plugin_list = [
    ThresholdingPlugin(simple_threshold.binary_threshold, 'binary threshold'),
    ThresholdingPlugin(simple_threshold.inverse_binary_threshold, 'inverse binary threshold'),
    ThresholdingPlugin(simple_threshold.halloween, 'halloween'),
    ThresholdingPlugin(simple_threshold.truncate_threshold, 'truncate threshold'),
    ThresholdingPlugin(simple_threshold.threshold_to_zero, 'threshold to zero'),
    PixelSortPlugin(body.pixelsort, 'pixel sort'),
    ThresholdingPlugin(simple_threshold.glitch, 'glitch (experimental)'),
    Plugin(copy.copy, 'copy')

]

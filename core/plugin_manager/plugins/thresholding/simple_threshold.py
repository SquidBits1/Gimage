from PIL import Image
import numpy as np
from dataclasses import dataclass


@dataclass
class ImagePlugin:

    @staticmethod
    def conv_to_gs(image):
        image = np.dot(image[..., 0:3], [0.299, 0.587, 0.114])
        return image

    def binary_threshold(self, image, threshold = 127):
        image = self.conv_to_gs(image)
        for cell in np.nditer(image, op_flags=['readwrite']):
            if cell > threshold:
                cell[...] = 255
            else:
                cell[...] = 0

        return image

    def inverse_binary_threshold(self, image, threshold = 127):
        image = self.conv_to_gs(image)
        for cell in np.nditer(image, op_flags=['readwrite']):
            if cell < threshold:
                cell[...] = 255
            else:
                cell[...] = 0

        return image

    # each individual colour is checked here

    def halloween(self, image, threshold = 127):
        copied = np.copy(image)
        for cell in np.nditer(copied, op_flags=['readwrite']):
            if cell > threshold:
                cell[...] = 255
            else:
                cell[...] = 0

        return copied

    def truncate_threshold(self, image, threshold = 127):
        image = self.conv_to_gs(image)
        for cell in np.nditer(image, op_flags=['readwrite']):
            if cell > threshold:
                cell[...] = threshold

        return image

    def threshold_to_zero(self, image, threshold = 127):
        image = self.conv_to_gs(image)
        for cell in np.nditer(image, op_flags=['readwrite']):
            if cell < threshold:
                cell[...] = 0

        return image

    def glitch(self, image, threshold = 127):
        copied = np.copy(image)
        for cell in np.nditer(copied, op_flags=['readwrite']):
            if cell > threshold:
                cell[...] = 0

        return copied

    def threshold_to_zero_inverse(self, image, threshold = 127):
        image = self.conv_to_gs(image)
        for cell in np.nditer(image, op_flags=['readwrite']):
            if cell > threshold:
                cell[...] = 0

        return image

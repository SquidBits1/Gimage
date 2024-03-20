"""
thresholding\simple_threshold.py -
This code contains the functions that do thresholds on images.
"""

import numpy as np


def conv_to_gs(image):
    """
    Converts an image to greyscale
    :param image: image to be converted
    :return:
    """
    if len(image.shape) != 3:
        return image
    # This applies a factor to each of the colour channels
    image = np.dot(image[..., 0:3], [0.299, 0.587, 0.114])
    return image


def apply_threshold(image, threshold=127, upper_value=255, lower_value=0):
    """
    Applies a threshold to an image.
    :param image: image data to be edited
    :param threshold: the threshold value
    :param upper_value: The value the pixel should go to if larger than threshold
    :param lower_value: The value the pixel should go to if smaller than threshold
    :return: edited image data
    """
    image = conv_to_gs(image)
    return np.where(image > threshold, upper_value, lower_value)


def binary_threshold(image, threshold=127):
    return apply_threshold(image, threshold)


def inverse_binary_threshold(image, threshold=127):
    return apply_threshold(image, threshold, upper_value=0, lower_value=255)


# each individual colour is checked here

def deepfry(image, threshold=127):
    copied = np.copy(image)
    for cell in np.nditer(copied, op_flags=['readwrite']):
        if cell > threshold:
            cell[...] = 255
        else:
            cell[...] = 0

    return copied


def deepfry_truncate(image, threshold=127):
    copied = np.copy(image)
    for cell in np.nditer(copied, op_flags=['readwrite']):
        if cell > threshold:
            cell[...] = 0

    return copied


def truncate_threshold(image, threshold=127):
    return apply_threshold(image, threshold, lower_value=threshold, upper_value=conv_to_gs(image))


def threshold_to_zero(image, threshold=127):
    return apply_threshold(image, threshold, lower_value=0, upper_value=conv_to_gs(image))


def threshold_to_zero_inverse(image, threshold=127):
    return apply_threshold(image, threshold, lower_value=conv_to_gs(image), upper_value=0)

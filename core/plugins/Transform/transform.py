"""
Transform\transform.py -
This file contains the functions to apply transform functions on an image.
"""

import numpy as np


def rotate(image, rotations):
    return np.rot90(image, k=rotations)


def flip(image):
    return np.fliplr(image)

def copy(image):
    return image.copy()
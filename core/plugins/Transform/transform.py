import numpy as np


def rotate(image, rotations):
    return np.rot90(image, k=rotations)


def flip(image):
    return np.fliplr(image)

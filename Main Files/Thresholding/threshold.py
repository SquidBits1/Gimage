from PIL import Image
import numpy as np

img = Image.open("castle.jpg")
img = np.array(img)
# converts image to greyscale
img = np.dot(img[..., 0:3], [0.299, 0.587, 0.114])


def binary_threshold(image, threshold):
    for cell in np.nditer(image, op_flags=['readwrite']):
        if cell > threshold:
            cell[...] = 255
        else:
            cell[...] = 0

    return image


def inverse_binary_threshold(image, threshold):
    for cell in np.nditer(image, op_flags=['readwrite']):
        if cell < threshold:
            cell[...] = 255
        else:
            cell[...] = 0

    return image


def truncate_threshold(image, threshold):
    for cell in np.nditer(image, op_flags=['readwrite']):
        if cell > threshold:
            cell[...] = threshold

    return image


def threshold_to_zero(image, threshold):
    for cell in np.nditer(image, op_flags=['readwrite']):
        if cell < threshold:
            cell[...] = 0

    return image


def threshold_to_zero_inverse(image, threshold):
    for cell in np.nditer(image, op_flags=['readwrite']):
        if cell > threshold:
            cell[...] = 0

    return image

img = Image.fromarray(img).convert('RGB')
img.save('threshold.png')

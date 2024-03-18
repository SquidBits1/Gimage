import numpy as np


def rgb_factors(image: np.ndarray, image_filter: np.ndarray):
    """
    Applies a filter to an image by performing a dot product
    :param image: An image of shape (width, height, 3)
    :param image_filter: A filter of shape (3, 3)
    :return: A filtered image
    """

    # discards images that don't have the correct shape
    if len(image.shape) != 3:
        return image

    # creates filtered image by performing a dot product on the r, g, b values and the filter transposed
    new_image = image.dot(image_filter.T)
    # rescales image
    new_image = np.divide(new_image, new_image.max(), out=new_image, casting="unsafe")

    return (new_image * 255).astype(np.uint8)


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

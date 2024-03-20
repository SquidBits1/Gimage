"""
pixel_sorting\pixel_sort.py -
The functions to pixel sort an image are contained here.
"""

import numpy as np
from core.plugins.pixel_sorting import sorting_functions


def sort_row(row, sorting_function):
    """
    Sorts one row of pixels up to the darkest pixel
    :param row: a NumPy array of pixels
    :param sorting_function: a function to convert a row from pixels to the sorting parameter
    :return: a sorted row array
    """
    # sums all the pixel values to find a basic pixel "brightness" value
    if sorting_function != sorting_functions.do_nothing:
        summed = sorting_function(row[:, :4])
    else:
        summed = sorting_function(row)
    min_index = np.argmin(summed)

    # sorts the row up to min_index
    summed_section = sorting_function(row[:min_index + 1])
    sorted_section = np.argsort(summed_section)
    # creates the final array by concatenating the new section with the old section
    final_arr = np.concatenate((row[:min_index + 1][sorted_section], row[min_index + 1:]), axis=0)
    return final_arr


def pixelsort(image, rotation=0, sorting_func=sorting_functions.luminance):
    """
    Pixel sorts an image
    :param image: image array data
    :param rotation: determines whether it sorts from up-down, left-right etc.
    :param sorting_func: a function to convert a row from pixels to the sorting parameter
    :return: A fully pixel-sorted image
    """
    # This means that the image may be greyscale
    if len(image.shape) < 3:
        sorting_func = sorting_functions.do_nothing
    # rotates image by value given
    image = np.rot90(image, k=rotation)
    new_array = np.empty_like(image)
    for i, column in enumerate(image):
        new_array[i] = sort_row(column, sorting_func)

    # undoes rotation image
    new_array = np.rot90(new_array, k=4 - rotation)

    return new_array

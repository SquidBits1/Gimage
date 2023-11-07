from PIL import Image
import numpy as np

from . import sorting_functions


def sort_row(row, sorting_function):
    # sums all the pixel values to find a basic pixel "brightness" value
    summed = sorting_function(row[:, :4])
    min_index = np.argmin(summed)

    # sorts the row up to min_index
    summed_section = sorting_function(row[:min_index + 1])
    sorted_section = np.argsort(summed_section)
    # creates the final array by concatenating the new section with the old section
    final_arr = np.concatenate((row[:min_index + 1][sorted_section], row[min_index + 1:]), axis=0)
    return final_arr


def pixelsort(image, rotation=0, sorting_func=sorting_functions.luminance):
    # rotates image by value given
    image = np.rot90(image, k=rotation)
    new_array = np.empty_like(image)
    for i, column in enumerate(image):
        new_array[i] = sort_row(column, sorting_func)

    # undoes rotation image
    new_array = np.rot90(new_array, k=4 - rotation)

    return new_array


if __name__ == '__main__':
    img = Image.open("C:/Users/gilsmi0809/PycharmProjects/pixel_sorting/Main Files/test_images\castle.jpg")

    img_a = np.array(img)
    img_b = pixelsort(img_a, 0)
    img_b = Image.fromarray(img_b)
    img_b.save('sorted.jpg')

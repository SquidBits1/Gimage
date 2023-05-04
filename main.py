from PIL import Image
import numpy as np

img = Image.open('Bamburgh_Castle,_beautiful_day.jpg')

img_a = np.array(img)


def luminance(row):
    temp = np.zeros_like(row)
    temp[:, 0] = row[:, 0] * 0.2126
    temp[:, 1] = row[:, 1] * 0.7152
    temp[:, 2] = row[:, 2] * 0.0722
    return np.sum(temp, axis=1)

    # TODO convert luminance back to rgb


def sum(row):
    return np.sum(row, axis=1)


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


def pixelsort(image, rotation=0, sorting_func=sum):
    # rotates image by value given
    image = np.rot90(image, k=rotation)
    new_array = np.empty_like(image)
    for i, column in enumerate(image):
        new_array[i] = sort_row(column, sorting_func)

    # undoes rotation image
    new_array = np.rot90(new_array, k=4 - rotation)

    return new_array


img_b = pixelsort(img_a, 2, sum)
img_b = Image.fromarray(img_b)
img_b.save('sorted.jpg')

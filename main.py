from PIL import Image
import numpy as np

img = Image.open('Bamburgh_Castle,_beautiful_day.jpg')

img_a = np.array(img)


def sort_row(row):
    # sums all the pixel values to find a basic pixel "brightness" value
    summed = np.sum(row[:, :4], axis=1)
    min_index = np.argmin(summed)

    # sorts the row up to min_index
    sorted_section = np.argsort(row[:min_index + 1].sum(axis=1))
    # creates the final array by concatenating the new section with the old section
    final_arr = np.concatenate((row[:min_index + 1][sorted_section], row[min_index + 1:]), axis=0)
    return final_arr


test = sort_row(img_a[0])


def pixelsort(image, column=False):
    if column:
        image = np.rot90(image)
    new_array = np.empty_like(image)
    for i, column in enumerate(image):
        new_array[i] = sort_row(column)

    return new_array


column = True
img_b = pixelsort(img_a, column=column)
if column:
    img_b = np.rot90(img_b, k=3)
img_b = Image.fromarray(img_b)
img_b.save('sorted.jpg')

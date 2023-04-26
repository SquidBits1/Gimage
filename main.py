from PIL import Image
import numpy as np

img = Image.open('Bamburgh_Castle,_beautiful_day.jpg')

img_a = np.array(img)


def sort_column(column):
    # sums all the pixel values to find a basic pixel "brightness" value
    summed = np.sum(column[:,:4], axis=1)
    min_index = np.argmin(summed)
    print(min_index)

    # sorts the row up to min_index
    sorted_section = np.argsort(column[:min_index + 1].sum(axis=1))
    # creates the final array by concatenating the new section with the old section
    final_arr = np.concatenate((column[:min_index + 1][sorted_section], column[min_index + 1:]), axis=0)
    return final_arr


test = sort_column(img_a[0])



def sort_columns(image):
    new_array = np.empty_like(image)
    for i, column in enumerate(image):
        new_array[i] = sort_column(column)

    return new_array

img_b = sort_columns(img_a)
img_b = Image.fromarray(img_b)
img_b.save('sorted.jpg')
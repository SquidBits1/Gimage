import numpy as np

# creates a filter where every thing is weighted by same amount
kernel = np.array([1 / 9, 1 / 9, 1 / 9])


# performs a convolution using an image and a filter
# def convolve(image, image_filter):
#     # you have to pad the image so that it doesn't reach edges
#     padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2), dtype=int)
#     padded[1:-1, 1:-1] = image[:]
#
#     output = np.zeros_like(padded)
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             output[i, j] = (image_filter * padded[i:i + 3, j:j + 3]).sum()
#
#     return output[1:-1, 1:-1]


# def blur(image, image_filter=kernel):
#     print(image.shape)
#     colours = [np.reshape(i, (i.shape[0], i.shape[1])) for i in np.split(image, indices_or_sections=3, axis=2)]
#     colours_blurred = []
#     for colour_array in colours:
#         a = np.apply_along_axis(lambda x: np.convolve(x, image_filter, mode='same'), 0, colour_array)
#         a = np.apply_along_axis(lambda x: np.convolve(x, image_filter, mode='same'), 1, a)
#         colours_blurred.append(a)
#     colours = [np.reshape(i, (i.shape[0], i.shape[1], 1)) for i in colours_blurred]
#     final = np.rint(np.concatenate(colours, axis=2)).astype(int)
#     print(final.shape)
#     return final
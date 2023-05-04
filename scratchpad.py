# def sort_image(image):
#     summed = np.sum(image, axis=2)
#     indexes = np.argmin(summed, axis=1)
#     grid = np.zeros_like(summed)
#     print(indexes)
#
#     sorted_section = np.argsort(summed[:, indexes], axis=1)
#     print(sorted_section.shape)
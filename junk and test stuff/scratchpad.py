import numpy as np
from PIL import Image

img = Image.open('../Main Files/igrj11014_4k.jpg')

img_a = np.array(img)


def sort_image(image):
    # TODO IMPORTANT does not factor out transparency work on this later
    summed = np.sum(image, axis=2)
    indexes = np.argmin(summed, axis=1)
    final = np.zeros_like(summed)

    for i, index in enumerate(indexes):
        final[i, :index + 1] = summed[i, :index + 1]

    final = np.sort(final, axis=1)


sort_image(img_a)

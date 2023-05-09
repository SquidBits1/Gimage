from PIL import Image
import numpy as np

img = Image.open("castle.jpg")
img = np.array(img)


# test = np.array([[[255, 0, 0], [34, 111, 0]], [[0, 0, 225], [1, 1, 141]]])


def img2grey(image):
    grey = np.dot(image[..., 0:3], [0.299, 0.587, 0.114])
    return grey


def binary_threshold(image, threshold):
    image = img2grey(image)
    for cell in np.nditer(image, op_flags=['readwrite']):
        if cell > threshold:
            cell[...] = 255
        else:
            cell[...] = 0

    return image


img = binary_threshold(img, 190)
print(img.shape)
img = Image.fromarray(img).convert('RGB')
img.save('threshold.png')

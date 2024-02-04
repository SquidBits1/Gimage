from PIL import Image
import numpy as np


img = Image.open("../core/plugins/thresholding/castle.jpg")
img = np.array(img)
# converts image to greyscale
img = np.dot(img[..., 0:3], [0.299, 0.587, 0.114])


# Finds the normalised histogram of the image
def histogram(image):
    hist = np.histogram(image, bins=np.arange(256), density=True)
    return hist


probability, bins = histogram(img)

q = probability.cumsum()
print(q)
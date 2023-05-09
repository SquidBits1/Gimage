import cv2
import numpy as np

img = cv2.imread('castle.jpg', 1)

thresh_low = 90
thresh_high = 200

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, low = cv2.threshold(grey, thresh_low, 255, cv2.THRESH_BINARY)
ret2, high = cv2.threshold(grey, thresh_high, 255, cv2.THRESH_BINARY_INV)
full_mask = cv2.bitwise_and(low, high)

a = lambda row: np.convolve(row, [-1, 1], 'same')

edges = np.apply_along_axis(a,0,full_mask)

intervals = [np.flatnonzero(row) for row in edges]

for row, key in enumerate(full_mask):
    order = np.split(key, intervals[row])
    if row == 0:
        print(order)
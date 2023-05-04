import cv2
import numpy as np

img = cv2.imread('Bamburgh_Castle,_beautiful_day.jpg', 1)

thresh_low = 90
thresh_high = 200

grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, low = cv2.threshold(grey, thresh_low, 255, cv2.THRESH_BINARY)
ret2, high = cv2.threshold(grey, thresh_high, 255, cv2.THRESH_BINARY_INV)
full_mask = cv2.bitwise_and(low, high)
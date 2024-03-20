"""
Filters\filters.py -
This file contains the filter matrices used for the filters plugin packages!
"""

import numpy as np

sepia_filter = np.array([[.393, .769, .189],
                         [.349, .686, .168],
                         [.272, .534, .131]])

red_filter = np.array([[1, 1, 1],
                         [1, 0.01, 0.01],
                         [1, 0.01, 0.01]])

green_filter = np.array([[.01, 1, .01],
                         [1, 1, 1],
                         [.01, 1, 0.01]])

blue_filter = np.array([[.1, .1, 1],
                         [.1, 0.1, 1],
                         [1, 1, 1]])
import numpy as np


def luminance(row):
    temp = np.zeros_like(row)
    temp[:, 0] = row[:, 0] * 0.2126
    temp[:, 1] = row[:, 1] * 0.7152
    temp[:, 2] = row[:, 2] * 0.0722
    return np.sum(temp, axis=1)



def basic_sum(row):
    return np.sum(row, axis=1)

import numpy as np


def luminance(row):
    """
    Calculates luminance of each pixel in a row
    :param row:
    :return:
    """
    temp = np.empty_like(row)
    temp[:, 0] = row[:, 0] * 0.2126
    temp[:, 1] = row[:, 1] * 0.7152
    temp[:, 2] = row[:, 2] * 0.0722
    return np.sum(temp, axis=1)


# If image is already gs, it returns the row without doing anything to it
def do_nothing(row):
    return row


def basic_sum(row):
    return np.sum(row, axis=1)


def red(row):
    return row[:, 0]


def green(row):
    return row[:, 1]


def blue(row):
    return row[:, 2]

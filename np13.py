import numpy as np


def convert_2d(arr) -> np.array:
    """
    Function that converts (in sequence depth wise (along third axis))
    two 1-D arrays into a 2-D array.
    """
    array = np.dstack((arr[0], arr[1]))
    return array




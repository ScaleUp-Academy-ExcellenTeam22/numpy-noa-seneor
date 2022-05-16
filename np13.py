import numpy as np


def convert_2d(arr):
    """
    Function that convert (in sequence depth wise (along third axis))
    two 1-D arrays into a 2-D array.
    """
    array = np.dstack((arr[0], arr[1]))
    return array


if __name__ == '__main__':
    a = np.array([10, 20, 30])
    b = np.array([40, 50, 60])
    print(convert_2d(np.array([a, b])))


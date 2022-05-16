import numpy as np


def median_array(array):
    """
    Function that compute the median of flattened given array
    """
    return np.median(array)


if __name__ == '__main__':
    arr = np.array([[0, 1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11]])
    print(median_array(arr))

import numpy as np


def diagonal_array():
    """
    Function that create a 3-D array with ones on a diagonal and zeros elsewhere
    """
    array = np.zeros((3, 3))
    np.fill_diagonal(array, 1, wrap=True)
    return array


if __name__ == '__main__':
    print(diagonal_array())



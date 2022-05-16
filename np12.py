import numpy as np


def remove_single(shape):
    """
    Function that remove single-dimensional entries from a specified shape
    """
    array = np.zeros(shape)
    print(np.squeeze(array).shape)


if __name__ == '__main__':
    remove_single((3, 1, 4))



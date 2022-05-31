import numpy as np


def remove_single(array_shape) -> tuple:
    """
    Function that removes single-dimensional entries from a specified shape
    """
    array = np.zeros(array_shape)
    return (np.squeeze(array).shape)

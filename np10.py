import numpy as np


def sort_axis(array) -> tuple:
    """
    Function that sorts along the first, last axis of a given array
    """
    first_axis = np.sort(array, axis=0)
    last_axis = np.sort(first_axis, axis=1)
    return first_axis, last_axis

import numpy as np


def swap_last_first() -> np.array:
    """
    Function that creates a 4x4 array with random values,
    then returns a new array from the said array swapping first and last rows
    """
    matrix = np.random.random((4, 4))
    new_matrix = np.vstack([matrix[matrix.shape[0]-1], matrix[1:3], matrix[0]])
    return new_matrix


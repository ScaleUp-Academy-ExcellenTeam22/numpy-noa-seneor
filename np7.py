import numpy as np


def swap_last_first():
    """
    Function that create a 4x4 array with random values,
    then create a new array from the said array swapping first and last rows
    :return: Matrix
    """
    matrix = np.arange(16).reshape(-1, 4)
    print(f"before:\n {matrix}")
    new_matrix = np.vstack([matrix[matrix.shape[0]-1], matrix[1:3], matrix[0]])
    print(f"after:\n {new_matrix}")


if __name__ == '__main__':
    print(swap_last_first())


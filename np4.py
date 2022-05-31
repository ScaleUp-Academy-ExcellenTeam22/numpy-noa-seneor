import numpy as np


def border_matrix() -> np.array:
    """
    Function that returns a 10d array with 1 in the border and 0 inside
    """
    matrix =np.ones((10,10))
    matrix[1:-1,1:-1] = 0
    return matrix


if __name__ == '__main__':
    print(border_matrix())


import numpy as np


def border_matrix():
    """
    Function that create a 10x10 matrix where elements in the border equals to 1
    the rest 0
    :return: matrix
    """
    matrix = np.random.randint(0, 1, 100)
    matrix = matrix.reshape((10, 10))
    matrix[0] = 1
    matrix[9] = 1
    matrix[:, 0] = 1
    matrix[:, 9] = 1
    return matrix


if __name__ == '__main__':
    print(border_matrix())


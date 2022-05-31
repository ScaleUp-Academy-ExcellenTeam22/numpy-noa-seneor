import numpy as np


def np_vector() -> np.arange:
    """
    Function that create a vector with values from 0 to 20
    and change the sign of the numbers in the range from 9 to 15
    :return: Vector
    """
    vector = np.arange(21)
    vector[9:16] *= -1
    return vector


if __name__ == '__main__':
    print(np_vector())


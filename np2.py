import numpy as np


def np_random_vector():
    """
    Function that creates a vector of length 10 with values
    evenly distributed between 5 and 50
    :return: Vector
    """
    vector = np.random.randint(5, 51, 10)
    return vector


if __name__ == '__main__':
    print(np_random_vector())


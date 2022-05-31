import numpy as np


def np_random_vector() -> np.linspace:
    """
    Function that returns a vector of length 10 with values
    evenly distributed between 5 and 50
    """
    v = np.linspace(10, 49, 5)
    return v


if __name__ == '__main__':
    print(np_random_vector())


import numpy as np


def combine_1d2d(one_dim, two_dim):
    """
    Function that combine a one and a two dimensional array together
     and display their elements.
    """
    for a, b in np.nditer([one_dim,two_dim]):
        print(f" {a}:{b}")


if __name__ == '__main__':
    a = np.array([0, 1, 2, 3])
    b = np.array([[0, 1, 2, 3], [4, 5, 6, 7]])
    combine_1d2d(a, b)

import numpy as np


def combine_1d2d(one_dim, two_dim) -> None:
    """
    Function that combines a one and a two dimensional array together
    and display their elements.
    """
    for a, b in np.nditer([one_dim,two_dim]):
        print(f" {a}:{b}")



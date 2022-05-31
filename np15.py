import numpy as np


def create_0_255_array() -> np.array:
    """
    Function that creates a three-dimension array with shape (300,400,5) and
    fill the array elements with value between 0 and 255
    """
    array = np.random.randint(0, 256, (300, 400, 5))
    return array

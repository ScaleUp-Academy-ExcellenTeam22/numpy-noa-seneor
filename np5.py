import numpy as np


def add_vector_to_matrix(vector, matrix) -> np.array:
    """
    Function that adds a vector to each row of a given matrix
    """
    matrix += vector
    return matrix




import numpy as np


def add_vector_to_matrix(vector, matrix):
    """
    Function that add a vector to each row of a given matrix
    :return: matrix
    """
    for i in range(matrix.shape[0]):
        matrix[i] += vector
    return matrix




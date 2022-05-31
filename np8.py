import numpy as np


def replace_array(array, num, replacer) -> np.array:
    """
    Function that replaces all numbers in a given array
    that are equal, less and greater to a given number
    """
    
    array = np.where(array == num, replacer, array)
    array = np.where(array < num, replacer, array)
    array =np.where(array > num, replacer, array)
    return array

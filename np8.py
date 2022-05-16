import numpy as np


def replace_array(array, num, replacer):
    """
    Function that replace all numbers in a given array
    which is equal, less and greater to a given number
    :return: Replaced Arrays
    """
    print(f"\nReplace all elements equal to {num} by {replacer} ")
    print(np.where(array == num, replacer, array))
    print(f"\nReplace all elements less than {num} by {replacer} ")
    print(np.where(array < num, replacer, array))
    print(f"\nReplace all elements greater than {num} by {replacer} ")
    print(np.where(array > num, replacer, array))




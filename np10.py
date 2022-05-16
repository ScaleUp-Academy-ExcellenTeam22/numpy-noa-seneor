import numpy as np


def sort_axis(array):
    """
    Function that sort an along the first, last axis of a given array
    """
    first_axis = np.sort(array, axis=0)
    print(f"sorted by 1st axis: \n {first_axis}")
    last_axis = np.sort(first_axis, axis=1)
    print(f"sorted by last axis: \n {last_axis}")


if __name__ == '__main__':
    sort_axis(np.array([[4, 6], [2, 1]]))




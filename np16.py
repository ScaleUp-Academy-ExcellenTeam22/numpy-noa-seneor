import numpy as np


def sort_student(student_id, student_height):
    """
    Function that sort the student id with increasing height
    Print the integer indices that
    describes the sort order by multiple columns and the sorted data
    """
    sorted_indexes = np.lexsort((student_id, student_height))
    print(sorted_indexes)
    print('sorted data:')
    for i in sorted_indexes:
        print(student_id[i], student_height[i])


if __name__ == '__main__':
    id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
    height = np.array([40., 42., 45., 41., 38., 40., 42.0])
    sort_student(id, height)

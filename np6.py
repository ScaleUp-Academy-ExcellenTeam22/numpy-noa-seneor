import matplotlib.pyplot as mplot
import numpy as np


def plot_sin(x):
    """
    Function that compute the x and y coordinates for points
    on a sine curve and plot the points using matplotlib
    :return: Vector
    """
    y = np.sin(x)
    mplot.plot(x, y)
    return mplot.show()


if __name__ == '__main__':
    print(plot_sin(np.arange(0, 3*np.pi, 0.2)))


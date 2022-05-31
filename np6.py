import matplotlib.pyplot as mplot
import numpy as np

def plot_sin(x) -> None:
    """
    Function that computes the x and y coordinates for points
    on a sine curve and plot the points using matplotlib
    """
    y = np.sin(x)
    mplot.plot(x, y)
    mplot.show()


plot_sin(np.arange(0, 3*np.pi, 0.2))


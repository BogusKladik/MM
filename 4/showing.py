import matplotlib.pyplot as plt
import numpy as np


def show_function_with_interval(f, interval):
    x = np.linspace(interval[0], interval[1], 100)
    plt.plot(x, f(x))
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()
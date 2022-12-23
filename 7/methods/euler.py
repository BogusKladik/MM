import numpy as np


def euler_method(interval, y, f, h, accuracy):
    n = int(((interval[1] - interval[0]) / h)) + 1

    data_x = np.linspace(interval[0], interval[1], n)
    data_y = [y]

    for i in range(1, n):
        data_y.append(round(data_y[i - 1] + h *
                      f(data_x[i - 1], data_y[i - 1]), accuracy))
    data_y = np.array(data_y)

    return (data_x, data_y)

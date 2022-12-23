import numpy as np


def rk4_method(interval, y, f, h, accuracy):
    n = int(((interval[1] - interval[0]) / h)) + 1

    data_x = np.linspace(interval[0], interval[1], n)
    data_y = [y]

    for i in range(1, n):
        K1 = f(data_x[i - 1], data_y[i - 1])
        K2 = f(data_x[i - 1] + h / 2, data_y[i - 1] + h / 2 * K1)
        K3 = f(data_x[i - 1] + h / 2, data_y[i - 1] + h / 2 * K2)
        K4 = f(data_x[i - 1] + h, data_y[i - 1] + h * K3)
        data_y.append(round(data_y[i - 1] + h / 6 *
                      (K1 + 2 * K2 + 2 * K3 + K4), accuracy))
    data_y = np.array(data_y)

    return (data_x, data_y)

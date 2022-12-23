import numpy as np


def solution(interval, f, h, acc):
    n = int(((interval[1] - interval[0]) / h)) + 1

    data_x = np.linspace(interval[0], interval[1], n)
    data_y = np.array([round(f(data_x[i]), acc) for i in range(n)])

    return (data_x, data_y)

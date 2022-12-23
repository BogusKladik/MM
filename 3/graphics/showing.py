from matplotlib import pyplot as plt
from managers.manager_math import draw_density_F, draw_density_f
from utils.math_utils import *


def plot_histogram(data_x: list, data_hist: list, k: int, interval: tuple[float, float], title: str, dstr: str, m: float = 0.0, d: float = 0.0, sigma: float = 0.0) -> None:
    delta = (interval[1] - interval[0]) / k
    for data in data_hist:
        x_min = data[1]
        x_max = data[2]
        gl = data[0]
        rl = (x_max + x_min) / 2
        plt.bar(rl, gl, width=delta, color="b")
    plt.title(title)
    draw_density_f(data_x, interval, dstr, m, d, sigma)
    plt.show()


def plot_polygon(data_x: list, data_polygon: list, interval: tuple[float, float], title: str, dstr: str, m: float = 0.0, d: float = 0.0, sigma: float = 0.0) -> None:
    x = [interval[0]]
    y = [0]
    for i in data_polygon:
        y.append(i[0])
        x.append(i[1])
    plt.step(x, y, color="b")
    plt.title(title)
    draw_density_F(data_x, interval, dstr, m, d, sigma)
    plt.show()

import math
from matplotlib import pyplot as plt
from utils.math_utils import F_gauss, F_normal, F_rayleigh, f_gauss, f_normal, f_rayleigh


def draw_density_f(data_x: list, interval: tuple[float, float], dstr: str, m: float = 0.0, d: float = 0.0, sigma: float = 0.0):
    match dstr:
        case "normal":
            r = []
            for x in data_x:
                r.append(f_normal(interval, x))
            plt.plot(data_x, r, color="r")
        case "gauss":
            r = []
            sigma = math.sqrt(d)
            for x in data_x:
                r.append(f_gauss(x, m, sigma))
            plt.plot(data_x, r, color="r")
        case "rayleigh":
            r = []
            for x in data_x:
                r.append(f_rayleigh(x, sigma))
            plt.plot(data_x, r, color="r")
        case _:
            print("Неправильное название функции плотности распределения")
            raise SystemExit(1)


def draw_density_F(data_x: list, interval: tuple[float, float], dstr: str, m: float = 0.0, d: float = 0.0, sigma: float = 0.0):
    match dstr:
        case "normal":
            r = []
            for x in data_x:
                r.append(F_normal(interval, x))
            plt.plot(data_x, r, color="r")
        case "gauss":
            r = []
            sigma = math.sqrt(d)
            for x in data_x:
                r.append(F_gauss(x, m, sigma))
            plt.plot(data_x, r, color="r")
        case "rayleigh":
            r = []
            for x in data_x:
                r.append(F_rayleigh(x, sigma))
            plt.plot(data_x, r, color="r")
        case _:
            print("Неправильное название функции")
            raise SystemExit(1)

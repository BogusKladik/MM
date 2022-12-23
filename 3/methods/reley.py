from create_sampling import *
from graphics.graphs_points import create_histogram, create_polygon
from graphics.showing import plot_histogram, plot_polygon
from utils.math_utils import *
import math
from prettytable import PrettyTable


def reley(sigma_rayleigh: float):
    def g(x): return rayleigh_distribution(x, sigma_rayleigh)
    x_neumann, interval_neumann = create_sampling_neiman(rayleigh_distribution(
        sigma_rayleigh, sigma_rayleigh), 0.0, 4 * sigma_rayleigh, g)
    data_hist_neumann, k_neumann = create_histogram(
        x_neumann, interval_neumann)
    data_polygon_neumann, _ = create_polygon(x_neumann, interval_neumann)

    plot_histogram(
        x_neumann,
        data_hist_neumann,
        k_neumann,
        interval_neumann,
        "Плотность вероятности распределения Релея (гистограма)",
        "rayleigh",
        sigma=sigma_rayleigh
    )
    plot_polygon(
        x_neumann,
        data_polygon_neumann,
        interval_neumann,
        "Функция распределения Релея (полигоны)",
        "rayleigh",
        sigma=sigma_rayleigh
    )

    m_theory = math.sqrt((math.pi * (sigma_rayleigh ** 2)) / 2)
    m_practice = find_mathematical_expectation(x_neumann)

    print("-----------------------------------------------------------------------------------")
    print("Теоретические данные")
    print("-----------------------------------------------------------------------------------")
    print(f"Математическое ожидание распределения Релея: {m_theory}")
    print(
        f"Дисперсия распределения Реле: {(2 - math.pi / 2) * (sigma_rayleigh ** 2)}")
    print("-----------------------------------------------------------------------------------")
    print("Практические данные")
    print("-----------------------------------------------------------------------------------")
    print(
        f"Математическое ожидание распределения Релея: {round(m_practice, 3)}")
    print(
        f"Дисперсия распределения Реле с теоретическим значением математического ожидания: {round(find_dispersion(x_neumann, m_theory), 3)}")
    print(
        f"Дисперсия распределения Реле с практическим значением математического ожидания: {round(find_dispersion(x_neumann, m_practice), 3)}")

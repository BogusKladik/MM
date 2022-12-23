from create_sampling import *
from graphics.graphs_points import create_histogram, create_polygon
from graphics.showing import plot_histogram, plot_polygon
from utils.math_utils import *


def gaussian(m_gauss: float, d_gauss: float) -> None:
    x_gauss, interval_gauss = create_sampling_CLT(m_gauss, d_gauss)
    data_hist_gauss, k_gauss = create_histogram(x_gauss, interval_gauss)
    data_polygon_gauss, _ = create_polygon(x_gauss, interval_gauss)

    plot_histogram(
        x_gauss,
        data_hist_gauss,
        k_gauss,
        interval_gauss,
        "Плотность вероятности распределения Гаусса (гистограма)",
        "gauss",
        m=m_gauss,
        d=d_gauss
    )
    plot_polygon(
        x_gauss,
        data_polygon_gauss,
        interval_gauss,
        "Функция распределения Гаусса (полигоны)",
        "gauss",
        m=m_gauss,
        d=d_gauss
    )

    m_practice = find_mathematical_expectation(x_gauss)

    print("-----------------------------------------------------------------------------------")
    print("Теоретические данные")
    print("-----------------------------------------------------------------------------------")
    print(f"Математическое ожидание распределения Гаусса: {m_gauss}")
    print(f"Дисперсия распределения Гаусса: {d_gauss}")
    print("-----------------------------------------------------------------------------------")
    print("Практические данные")
    print("-----------------------------------------------------------------------------------")
    print(
        f"Математическое ожидание распределения Гаусса: {round(m_practice, 3)}")
    print(
        f"Дисперсия распределения Гаусса с теоретическим значением математического ожидания: {round(find_dispersion(x_gauss, m_gauss), 3)}")
    print(
        f"Дисперсия распределения Гаусса с практическим значением математического ожидания: {round(find_dispersion(x_gauss, m_practice), 3)}")

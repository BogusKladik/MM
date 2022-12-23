from create_sampling import *
from graphics.graphs_points import create_histogram, create_polygon
from graphics.showing import plot_histogram, plot_polygon
from utils.math_utils import *


def reversed_functions(left_limit: float, right_limit: float) -> None:
    if left_limit == right_limit:
        print("Пределы не должны быть равными")
        raise SystemExit(1)

    if left_limit > right_limit:
        print("Левый предел больше правого, принято решение поменять их местами")
        temp = left_limit
        left_limit = right_limit
        right_limit = temp

    data_normal, interval_normal = create_normal_sampling(
        left_limit, right_limit)
    data_hist_normal, k_normal = create_histogram(data_normal, interval_normal)
    data_polygon_normal, _ = create_polygon(data_normal, interval_normal)

    plot_histogram(
        data_normal,
        data_hist_normal,
        k_normal,
        interval_normal,
        "Плотность вероятности равномерного распределения (гистограма)",
        "normal"
    )
    plot_polygon(
        data_normal,
        data_polygon_normal,
        interval_normal,
        "Функция равномерного распределения (полигоны)",
        "normal"
    )

    m_practice = find_mathematical_expectation(data_normal)

    print("-----------------------------------------------------------------------------------")
    print("Теоретические данные")
    print("-----------------------------------------------------------------------------------")
    print(
        f"Математическое ожидание равномерного распределения: {(right_limit + left_limit) / 2}")
    print(
        f"Дисперсия равномерного распределения: {(right_limit - left_limit)**2 / 12}")
    print("-----------------------------------------------------------------------------------")
    print("Практические данные")
    print("-----------------------------------------------------------------------------------")
    print(
        f"Математическое ожидание равномерного распределения: {round(m_practice, 3)}")
    print(
        f"Дисперсия равномерного распределения с теоретическим значением математического ожидания: {round(find_dispersion(data_normal, (right_limit + left_limit) / 2), 3)}")
    print(
        f"Дисперсия равномерного распределения с практическим значением математического ожидания: {round(find_dispersion(data_normal, m_practice), 3)}")

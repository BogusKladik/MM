import matplotlib.pyplot as plt
import numpy as np


def parabolic_interpolation(data_x: np.ndarray, data_y: np.ndarray, xi: float) -> float | None:
    yi = None
    for i in range(1, len(data_x) - 1):
        if (data_x[i - 1] <= xi < data_x[i]) or (data_x[i] <= xi <= data_x[i + 1]):
            solve = np.linalg.solve(np.array([np.array([data_x[i - 1]**2, data_x[i - 1], 1]),
                                              np.array([data_x[i]**2, data_x[i], 1]),
                                              np.array([data_x[i + 1]**2, data_x[i + 1], 1])]),
                                    np.array([data_y[i - 1], data_y[i], data_y[i + 1]]))

            ai, bi, ci = (solve[0], solve[1], solve[2])

            yi = ai * xi**2 + bi * xi + ci
            break

    return yi


def output_intermediate_value(data_x: np.ndarray, data_y: np.ndarray) -> None:
    lim_left, lim_right = (data_x[0], data_x[-1])

    while True:
        intermediate_value = float(
            input(f"Введите промежуточное значение по x между {lim_left} и {lim_right}: "))

        if lim_left <= intermediate_value <= lim_right:
            break

        print("Условия промежуточного значения не выполнены")

    print(
        f"При промежуточном значени по x = {intermediate_value}, значения функции по y = {parabolic_interpolation(data_x, data_y, intermediate_value)}")


def draw_parabolic_interpolation(data_x: np.ndarray, data_y: np.ndarray, nu: float = 0.01) -> None:
    data_xi = np.arange(data_x[0], data_x[-1], nu)
    data_yi = np.array([parabolic_interpolation(
        data_x, data_y, xi) for xi in data_xi])

    plt.scatter(data_x, data_y)
    plt.plot(data_xi, data_yi)

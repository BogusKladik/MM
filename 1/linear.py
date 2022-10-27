import matplotlib.pyplot as plt
import numpy as np


def linear_interpolation(data_x: np.ndarray, data_y: np.ndarray, xi: float) -> float | None:
    yi = None
    for i in range(len(data_x) - 1):
        if data_x[i] <= xi <= data_x[i + 1]:
            ai = (data_y[i + 1] - data_y[i]) / (data_x[i + 1] - data_x[i])
            bi = data_y[i] - ai * data_x[i]
            yi = ai * xi + bi
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
        f"При промежуточном значени по x = {intermediate_value}, значения функции по y = {linear_interpolation(data_x, data_y, intermediate_value)}")


def draw_linear_interpolation(data_x: np.ndarray, data_y: np.ndarray, nu: float = 0.01) -> None:
    data_xi = np.arange(data_x[0], data_x[-1], nu)
    data_yi = np.array([linear_interpolation(data_x, data_y, xi)
                       for xi in data_xi])

    plt.scatter(data_x, data_y)
    plt.plot(data_xi, data_yi)

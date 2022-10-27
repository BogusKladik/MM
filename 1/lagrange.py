import matplotlib.pyplot as plt
import numpy as np


def parameters_lagrange_interpolation(data_x: np.ndarray, data_y: np.ndarray, size: int = 3) -> np.ndarray:
    parameters = []

    for i in range(size):
        temp = 1
        for j in range(size):
            if i != j:
                temp *= data_x[i] - data_x[j]

        parameters.append(data_y[i] / temp)

    return np.array(parameters)


def lagrange_interpolation(data_x: np.ndarray, data_y: np.ndarray, xi: float) -> float:
    yi = 0.0
    parameters = parameters_lagrange_interpolation(data_x, data_y, len(data_x))
    for i in range(len(parameters)):
        temp = 1
        for j in range(len(parameters)):
            if i != j:
                temp *= xi - data_x[j]

        yi += temp * parameters[i]

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
        f"При промежуточном значени по x = {intermediate_value}, значения функции по y = {lagrange_interpolation(data_x, data_y, intermediate_value)}")


def draw_lagrange_interpolation(data_x: np.ndarray, data_y: np.ndarray, nu: float = 0.01) -> None:
    data_xi = np.arange(data_x[0], data_x[-1], nu)
    data_yi = np.array([lagrange_interpolation(
        data_x, data_y, xi) for xi in data_xi])

    plt.scatter(data_x, data_y)
    plt.plot(data_xi, data_yi)

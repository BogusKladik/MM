import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate


def inbuilt_interpolation(data_x: np.ndarray, data_y: np.ndarray, xi: float) -> float | None:
    yi = None

    temp = interpolate.splrep(data_x, data_y, s=0)
    yi = interpolate.splev(xi, temp, der=0)

    return yi  # type: ignore


def output_intermediate_value(data_x: np.ndarray, data_y: np.ndarray) -> None:
    lim_left, lim_right = (data_x[0], data_x[-1])

    while True:
        intermediate_value = float(
            input(f"Введите промежуточное значение по x между {lim_left} и {lim_right}: "))

        if lim_left <= intermediate_value <= lim_right:
            break

        print("Условия промежуточного значения не выполнены")

    print(
        f"При промежуточном значени по x = {intermediate_value}, значения функции по y = {inbuilt_interpolation(data_x, data_y, intermediate_value)}")


def draw_inbuilt_interpolation(data_x: np.ndarray, data_y: np.ndarray, nu: float = 0.01) -> None:
    data_xi = np.arange(data_x[0], data_x[-1], nu)
    temp = interpolate.splrep(data_x, data_y, s=0)
    data_yi = interpolate.splev(data_xi, temp, der=0)

    plt.scatter(data_x, data_y)
    plt.plot(data_xi, data_yi)

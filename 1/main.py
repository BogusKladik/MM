import sys

import matplotlib.pyplot as plt
import numpy as np

import inbuilt
import lagrange
import linear
import parabolic
import tools


def choice_method(data_x: np.ndarray, data_y: np.ndarray, method: str) -> None:
    match method:
        case "linear":
            linear.output_intermediate_value(data_x, data_y)
            linear.draw_linear_interpolation(data_x, data_y)
        case "parabolic":
            parabolic.output_intermediate_value(data_x, data_y)
            parabolic.draw_parabolic_interpolation(data_x, data_y)
        case "lagrange":
            lagrange.output_intermediate_value(data_x, data_y)
            lagrange.draw_lagrange_interpolation(data_x, data_y)
        case "inbuilt":
            inbuilt.output_intermediate_value(data_x, data_y)
            inbuilt.draw_inbuilt_interpolation(data_x, data_y)
        case _:
            sys.exit("Неправильное название метода")


def main() -> None:
    print("Введите какие графики вы хотите увидеть\nПример: 1 2 3 выведет 3 графика")

    while True:
        numbers_plots = list(
            map(int, input("Введите номер или номера графиков: ").split(' ')))

        data = []
        for number_plot in numbers_plots:
            data.append(tools.sort_read_data(number_plot))
        data = np.array(data, dtype=object)

        method = None
        while True:
            method = input(
                "Введите какой метод интерполяции вы хотите использовать (Доступные: linear, parabolic, lagrange, inbuilt) :")

            if method == "linear" or method == "parabolic" or method == "lagrange" or method == "inbuilt":
                break

            print("Неправильное название метода")

        for i in range(len(data)):
            print(
                f"Поиск промежуточного значения относительно графика №{numbers_plots[i]}")
            choice_method(data[i][0], data[i][1], method)

        plt.show()

        if input("Хотите продолжить? (y/n) ") == 'n':
            break


if __name__ == "__main__":
    main()

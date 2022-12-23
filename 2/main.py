from typing import Tuple

import matplotlib.pyplot as plt
import numpy as np

import tools


def gorner(parameters: np.ndarray, data_x: np.ndarray, power_polynom: int) -> float:
    result = parameters[0]
    for i in range(power_polynom, 0, -1):
        result *= data_x
        result += parameters[power_polynom - i + 1]

    return result


def sum_error(data_y: np.ndarray, data_gorner: np.ndarray) -> float:
    return ((data_y - data_gorner) ** 2).sum()


def approximation(data_x: np.ndarray, data_y: np.ndarray, power_polynom: int) -> Tuple[np.poly1d, np.ndarray]:
    data_c = np.polyfit(data_x, data_y, power_polynom)

    f = np.poly1d(data_c)

    return (f, data_c)


def draw_approximation(data_x: np.ndarray, data_y: np.ndarray, f: np.poly1d, nu: float = 0.01) -> None:
    data_xi = np.arange(data_x[0], data_x[-1], nu)

    plt.scatter(data_x, data_y)
    plt.plot(data_xi, f(data_xi))


def main() -> None:
    print("Введите какие графики вы хотите увидеть\nПример: 1 2 3 выведет 3 графика")

    while True:
        numbers_plots = list(
            map(int, input("Введите номер или номера графиков: ").split(' ')))

        data = np.array([tools.sort_read_data(number_plot)
                        for number_plot in numbers_plots])

        for i in range(len(data)):
            print(
                f"Вывод суммарной ошибки относительно графика №{numbers_plots[i]}")
            power_polynom = None
            while True:
                power_polynom = int(input(
                    f"Введите степень полинома, он должен быть меньше {len(data[i][0]) + 1}: "))

                if 0 <= power_polynom < len(data[i][0]) + 1:
                    break

            f, data_c = approximation(data[i][0], data[i][1], power_polynom)
            data_gorner = np.array(
                [gorner(data_c, x, power_polynom) for x in data[i][0]])
            draw_approximation(data[i][0], data[i][1], f)

            print(
                f"Суммарная ошибка отклонения: {sum_error(data[i][1], data_gorner)}")

        plt.show()

        if input("Хотите продолжить? (y/n) ") == 'n':
            break


if __name__ == "__main__":
    main()

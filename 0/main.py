import matplotlib.pyplot as plt


def read_data(number_file: int) -> list:
    data = []
    with open(f"data/{number_file}.data") as f:
        for nums in f:
            data.append(list(map(float, nums.split(' '))))

    return data


def main() -> None:
    print("Введите какие графики вы хотите увидеть\nПример: 1 2 3 выведет 3 графика")

    while True:
        numbers_plots = list(
            map(int, input("Введите номер или номера графиков: ").split(' ')))

        data = []
        for number_plot in numbers_plots:
            data.append(read_data(number_plot))

        print(data)

        for i in range(0, len(data)):
            plt.scatter(x=data[i][0], y=data[i][1])

        plt.show()

        if input("Хотите продолжить? (y/n)") == 'n':
            break


if __name__ == "__main__":
    main()

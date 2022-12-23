import matplotlib.pyplot as plt


def chord_method(f, x0, accuracy, iteration):
    x, x_prev, i = x0, x0 + 2 * accuracy, 0

    while abs(x - x_prev) >= accuracy:
        x, x_prev, i = x - f(x) / (f(x) - f(x_prev)) * (x - x_prev), x, i + 1
        data_x = [x_prev, x]
        data_y = [f(x_prev), f(x)]
        plt.scatter(data_x, data_y)
        if i == iteration:
            print(
                "Достигнут предел итераций, будет выведено значение скорее всего с другой точностью")
            break

    print("Решение находиться в точке по X: ",
          abs(int(x * 10**(abs(len(str(accuracy))) - 2)) / 10**(abs(len(str(accuracy))) - 2)))
    print("Колличество итераций: ", i)
    print("Точность вычислений: ", abs(int(f(x) * 10**(abs(len(str(accuracy))) - 2)) / 10**(abs(len(str(accuracy))) - 2)) if i == iteration else accuracy) 
    plt.scatter(x, f(x), color="red")


def chord_method1(f, x0, interval, accuracy, iteration):
    left_limit, right_limit = interval[0], interval[1]
    x, x_prev, i = left_limit - (right_limit - left_limit) / (f(right_limit) - f(left_limit)) * f(left_limit), x0, 0
    # x, x_prev, i = x0, x0 + 2 * accuracy, 0

    while abs(x - x_prev) >= accuracy:
        if f(x_prev) * f(left_limit) < 0:
            x, x_prev = x_prev - (x_prev - left_limit) / (f(x_prev) - f(right_limit)) * f(x_prev), x
        else:
            x, x_prev = x_prev - (right_limit - x_prev) / (f(right_limit) - f(x_prev)) * f(x_prev), x
        i += 1
        data_x = [x_prev, x]
        data_y = [f(x_prev), f(x)]
        plt.scatter(data_x, data_y)
        if i == iteration:
            print(
                "Достигнут предел итераций, будет выведено значение скорее всего с другой точностью")
            break
    print("Решение находиться в точке по X: ",
          abs(int(x * 10**(abs(len(str(accuracy))) - 2)) / 10**(abs(len(str(accuracy))) - 2)))
    print("Колличество итераций: ", i)
    print("Точность вычислений: ", abs(int(f(x) * 10**(abs(len(str(accuracy))) - 2)) / 10**(abs(len(str(accuracy))) - 2)) if i == iteration else accuracy) 
    plt.scatter(x, f(x), color="red")
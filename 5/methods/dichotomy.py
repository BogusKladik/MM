import matplotlib.pyplot as plt


def dichotomy_method(f, x0, interval, accuracy, iteration):
    x = x0
    left_limit = interval[0]
    right_limit = interval[1]
    i = 0
    while abs(right_limit - left_limit) >= 2 * accuracy:
        i += 1

        if f(x) == 0.0:
            break

        if f(left_limit) == 0.0:
            x = left_limit
            break

        if f(right_limit) == 0.0:
            x = right_limit
            break

        if f(left_limit) * f(x) < 0.0:
            right_limit = x
        else:
            left_limit = x

        x = (right_limit + left_limit) / 2.0

        if i == iteration:
            print(
                "Достигнут предел итераций, будет выведено значение скорее всего с другой точностью")
            break
    print("Решение находиться в точке по X: ",
          abs(int(x * 10**(abs(len(str(accuracy))) - 2)) / 10**(abs(len(str(accuracy))) - 2)))
    print("Колличество итераций: ", i)
    print("Точность вычислений: ", abs(int(f(x) * 10**(abs(len(str(accuracy))) - 2)) / 10**(abs(len(str(accuracy))) - 2)) if i == iteration else accuracy)
    plt.scatter(x, f(x), color="red")

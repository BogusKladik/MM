import matplotlib.pyplot as plt


def simple_iterations_method(f, g, x0, accuracy, iteration):
    x = x0
    x1 = g(x)
    i = 0
    while abs(x1 - x) >= accuracy:
        i += 1
        x = x1
        x1 = g(x)
        if i == iteration:
            print(
                "Достигнут предел итераций, будет выведено значение скорее всего с другой точностью")
            break
    print("Решение находиться в точке по X: ",
      abs(int(x * 10**(abs(len(str(accuracy))) - 2)) / 10**(abs(len(str(accuracy))) - 2)))
    print("Колличество итераций: ", i)
    print("Точность вычислений: ", abs(int(f(x) * 10**(abs(len(str(accuracy))) - 2)) / 10**(abs(len(str(accuracy))) - 2)) if i == iteration else accuracy) 
    plt.scatter(x, f(x), color="red")
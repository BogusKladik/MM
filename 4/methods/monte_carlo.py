import random
import numpy as np

def monte_carlo_v1(f, interval, n): 
    integral = 0
    # random.seed(11)
    r = [random.random() for _ in range(n)]
    u = [interval[0] + ri * (interval[1] - interval[0]) for ri in r]

    for ui in u:
        integral += f(ui)
    
    return abs((interval[1] - interval[0]) / n * integral)


def monte_carlo_v2(f, interval, n):
    max, min = function_max_min(f, interval)
    # random.seed(11)
    x = [interval[0] + random.random() * (interval[1] - interval[0]) for _ in range(n)]
    y = [min + random.random() * (max - min) for _ in range(n)]
    k = 0
    for i in range(n):
        if min < y[i] < f(x[i]):
            k += 1
    
    return (max - min) * (interval[1] - interval[0]) * k / n


def function_max_min(f, interval):
    x = np.linspace(interval[0], interval[1], 2112)
    y = np.array([f(xi) for xi in x])
    return max(y), min(y)
from utils.math_utils import *
from utils.utils import quicksort
import random


def create_normal_sampling(left_limit: float, right_limit: float) -> tuple[list, tuple[float, float]]:
    if left_limit == right_limit:
        print("Пределы не должны быть равными")
        raise SystemExit(1)
    
    if left_limit > right_limit:
        print("Левый предел больше правого, принято решение поменять их местами")
        temp = left_limit
        left_limit = right_limit
        right_limit = temp

    x = quicksort([random.random() * (right_limit - left_limit) + left_limit for _ in range(10000)])
    interval = (left_limit, right_limit)
    return x, interval


def create_sampling_CLT(m: float, d: float) -> tuple[list, tuple[float, float]]:
    sigma = math.sqrt(d)
    n = 12
    x = []
    for _ in range(2112):
        v = 0
        for _ in range(n):
            v += random.random()
        xi = gauss_distribution(v, m, sigma, n)
        x.append(xi)
    x = quicksort(x)
    interval = (x[0], x[-1])
    return x, interval


def create_sampling_neiman(max_y: float, left_limit: float, right_limit: float, g) -> tuple[list, tuple[float, float]]:
    ri = [random.random() for _ in range(4444)]
    rj = [random.random() for _ in range(4444)]
    data_x = []
    for i in range(4444):
        x = left_limit + (right_limit - left_limit) * ri[i]
        y = max_y * rj[i]
        if y <= g(x):
            data_x.append(x)
        if len(data_x) >= 2112:
            break
    data_x = quicksort(data_x)
    interval = (0, data_x[-1])
    return data_x, interval

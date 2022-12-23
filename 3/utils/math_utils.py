import math


def rayleigh_distribution(xl: float, sigma: float) -> float:
    return (xl / (sigma ** 2)) * math.exp(-1 * ((xl ** 2) / (2 * (sigma ** 2))))


def gauss_distribution(v: float, m: float, sigma: float, n: int) -> float:
    return sigma * math.sqrt(12 / n) * (v - (n / 2)) + m


def f_normal(interval: tuple[float, float], x: int) -> float:
    if interval[0] <= x <= interval[1]:
        return 1 / (interval[1] - interval[0])
    else:
        return 0


def F_normal(interval: tuple[float, float], x: float) -> float:
    if interval[0] <= x <= interval[1]:
        return (x - interval[0]) / (interval[1] - interval[0])
    elif x >= interval[1]:
        return 1
    else:
        return 0


def f_gauss(x: float, m: float, sigma: float) -> float:
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-1 * (x - m) ** 2 / (2 * (sigma ** 2)))


def F_gauss(x: float, m: float, sigma: float) -> float:
    return (1 / 2) * (1 + math.erf((x - m) / math.sqrt(2 * (sigma ** 2))))


def f_rayleigh(x: float, sigma: float) -> float:
    return (x / (sigma ** 2)) * math.exp(-1 * ((x ** 2) / (2 * (sigma ** 2))))


def F_rayleigh(x: float, sigma: float) -> float:
    return 1 - math.exp(-1 * (x ** 2) / (2 * sigma ** 2))


def find_mathematical_expectation(data: list) -> float:
    result = 0
    for x in data:
        result += x
    return result / len(data)


def find_dispersion(data: list, m: float) -> float:
    result = 0
    for x in data:
        result += (x - m)**2
    return result / len(data)

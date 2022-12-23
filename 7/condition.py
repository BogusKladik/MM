import math


def function_as_string(a, b, l, n):
    return f"y' = {(-1)**n} * {a} * y + {b} * x^2 + {l}"


def function(a, b, l, n):
    return lambda x, y: (-1)**n * a * y + b * x**2 + l


def cauchy_function(a, b, l, n):
    K = b / (-1 * (-1)**n * a)
    L = (2 * b) / (-1 * a**2)
    M = ((2 * b) / (-1 * a**2) - l) / ((-1)**n * a)
    return lambda x: (1 - M) * math.exp((-1)**n * a * x) + K * x**2 + L * x + M

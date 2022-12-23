import math


def function_as_string():
    return "x^2 * sin(x)"


def function():
    return lambda x: x**2 * math.sin(x)

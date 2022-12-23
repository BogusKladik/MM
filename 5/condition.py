import math


def function_as_string():
    return "tg(ax) - bx = 0"


def function():
    return lambda a, b, x: math.tan(a * x) - b * x


def f_function1():
    return lambda a, x: math.tan(a * x)


def f_function2():
    return lambda b, x: b * x


def g_function1():
    return lambda a, b, x: math.tan(a * x) / b


def g_function2():
    return lambda a, b, x: math.atan(b * x) / a


def differential_function():
    return lambda a, b, x: 1.0 / math.cos(a * x)**2 * a - b

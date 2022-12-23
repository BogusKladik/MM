import math
import numpy as np


# def function():
#     return lambda x: x**2


# def interval():
#     return (0.3, 3.0)

def function():
    return lambda x: np.cos(x)

def interval():
    return (-1.0, 1.5)

# def solution():
#     return 8.991

def solution():
    return 1.83897

def print_solution():
    print("Первообразная от x^2 = x^3/3\nОпределенный интеграл в интервале от 0.3 до 3 = 8.991")
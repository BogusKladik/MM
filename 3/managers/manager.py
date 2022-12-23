from methods.gaussian import gaussian
from methods.reley import reley
from methods.reversed import reversed_functions


def manager(option: int):
    match option:
        case 1:
            reversed_functions(float(input("Введите значение левого предела: ")), float(
                input("Введите значение правого предела: ")))
        case 2:
            gaussian(float(input("Математическое ожидание для распределения Гаусса: ")), float(
                input("Дисперсия для распределения Гаусса: ")))
        case 3:
            reley(float(input("Сигма для метода Неймана: ")))
        case _:
            print("Указанного значения не присутствует в выборе метода")

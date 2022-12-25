def accuracy(function_integral, expect, percent):
    current_percent = 1
    n = 1
    current = abs(function_integral(n))
    current_percent = abs((expect - current) / expect)

    while current_percent > percent:
        n *= 2
        current = function_integral(n)
        current_percent = abs((expect - current) / expect)

    return current, n


def accuracy_mc(function_integral, percent):
    current_percent = 1
    n = 1
    prev = abs(function_integral(n))

    current = 0
    while current_percent > percent:
        n *= 2
        current = abs(function_integral(n))
        current_percent = abs(current - prev)
        prev = current

    return current, n

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
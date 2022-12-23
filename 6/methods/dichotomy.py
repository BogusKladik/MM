def dichotomy_method(f, interval, accuracy):
    left_limit, right_limit = interval[0], interval[1]
    iteration = 1
    while abs(right_limit - left_limit) >= accuracy:
        x = (left_limit + right_limit) / 2
        if f(x - accuracy / 2) < f(x + accuracy / 2):
            right_limit = x
        else:
            left_limit = x
        iteration += 2

    return (left_limit, right_limit, iteration)

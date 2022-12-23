from scipy.constants import golden_ratio

def golden_ratio_method(f, interval, accuracy):
    left_limit, right_limit = interval[0], interval[1]
    golden = golden_ratio
    iteration = 1
    while abs(right_limit - left_limit) >= accuracy:
        x1 = right_limit - (right_limit - left_limit) / golden
        x2 = left_limit + (right_limit - left_limit) / golden
        if f(x1) < f(x2):
            right_limit = x2
        else:
            left_limit = x1
        iteration += 1
    return (left_limit, right_limit, iteration)

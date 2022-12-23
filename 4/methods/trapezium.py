def trapezium(f, interval, n):
    h = (interval[1] - interval[0]) / n

    integral = 0
    for i in range(n):
        integral += f(interval[0] + h * i)
    
    return abs(h * (integral + (f(interval[0]) + f (interval[1])) / 2))
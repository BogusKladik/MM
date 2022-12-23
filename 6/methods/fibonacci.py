def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_method(f, interval, accuracy, iteration):
    left_limit, right_limit = interval[0], interval[1]
    iteration_in = 1
    fibonacci_array = [0, 1]
    for i in range(2, iteration + 1):
        fibonacci_array.append(fibonacci_array[i - 1] + fibonacci_array[i - 2])

    while abs(right_limit - left_limit) >= accuracy:
        # x1 = left_limit + fibonacci(iteration_in - 2) / fibonacci(iteration_in) * (right_limit - left_limit)
        # x2 = left_limit + fibonacci(iteration_in - 1) / fibonacci(iteration_in) * (right_limit - left_limit)
        # x1 = right_limit - fibonacci(iteration_in - 1) / fibonacci(iteration_in) * (right_limit - left_limit)
        # x2 = left_limit + fibonacci(iteration_in - 2) / fibonacci(iteration_in) * (right_limit - left_limit)
        x1 = left_limit + fibonacci_array[iteration - iteration_in - 1] / fibonacci_array[iteration - iteration_in + 1] * (right_limit - left_limit)
        x2 = left_limit + fibonacci_array[iteration - iteration_in] / fibonacci_array[iteration - iteration_in + 1] * (right_limit - left_limit)
        if f(x1) > f(x2):
            left_limit = x1
        else:
            right_limit = x2
        iteration_in += 1
        if iteration_in == iteration:
            break

    return (left_limit, right_limit, iteration_in)

def fib(f, interval, accuracy, iteration):
    left_limit, right_limit = interval[0], interval[1]
    iteration_in = 1
    fibonacci_array = [0, 1]
    for i in range(2, iteration + 2):
        fibonacci_array.append(fibonacci_array[i - 1] + fibonacci_array[i - 2])
    
    d = right_limit - left_limit
    k = 1
    while abs(right_limit - left_limit) >= accuracy:
        d = d * fibonacci_array[iteration - iteration_in] / fibonacci_array[iteration - iteration_in + 1]
        x1 = right_limit - d
        x2 = left_limit + d
        if f(x1) <= f(x2):
            right_limit = x2
        else:
            left_limit = x1
        if iteration_in == iteration - 1:
            break
        iteration_in += 1
    return (left_limit + right_limit) / 2, iteration_in
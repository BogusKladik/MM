def frange(start: float, stop: float, step: float = 1.0):
    i = start
    while i < stop:
        yield i
        i += step


def read_data(number_file: int) -> list:
    data = []
    with open(f"data/{number_file}.data") as f:
        for nums in f:
            data.append(list(map(float, nums.split(' '))))

    return data


def sort_read_data(number_file: int) -> list:
    data = read_data(number_file)

    data_s = sorted(zip(data[0], data[1]), key=lambda tup: tup[0])

    data[0] = [x[0] for x in data_s]
    data[1] = [x[1] for x in data_s]

    return data

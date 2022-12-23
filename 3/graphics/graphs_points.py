import math


def create_histogram(data: list, interval: tuple[float, float]) -> tuple[list, int]:
    count_data = len(data)
    count_intervals = int(1 + 4.2 * math.log2(count_data))
    sample_size = interval[1] - interval[0]
    width_interval = sample_size / count_intervals

    data_hist = []
    for i in range(count_intervals):
        min = interval[0] + width_interval * i
        max = interval[0] + width_interval * (i + 1)

        count_elements = 0
        for x in data:
            if min < x <= max:
                count_elements += 1

            if x > max:
                break

        w = count_elements / (count_data * width_interval)
        data_hist.append([w, min, max])

    return data_hist, count_intervals


def create_polygon(data: list, interval: tuple[float, float]) -> tuple[list, int]:
    count_data = len(data)
    count_intervals = int(1 + math.log2(count_data))
    sample_size = interval[1] - interval[0]
    width_interval = sample_size / count_intervals

    data_polygon = []
    for i in range(count_intervals):
        right_limit = interval[0] + width_interval * (i + 1)

        count_elements = 0
        for x in data:
            if x < right_limit:
                count_elements += 1

        f = count_elements / count_data
        data_polygon.append([f, right_limit])

    return data_polygon, count_intervals

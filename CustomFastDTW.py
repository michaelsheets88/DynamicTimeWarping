import numbers
import numpy as np
from collections import defaultdict


def fastdtw_with_input_prep(x, y, radius=1, dist=None):
    x, y, dist = prep_inputs(x, y, dist)
    return fastdtw(x, y, radius, dist)


def difference(a, b):
    return abs(a - b)


def norm(p):
    return lambda a, b: np.linalg.norm(a - b, p)


def fastdtw(x, y, radius, dist):
    min_time_size = radius + 2

    if len(x) < min_time_size or len(y) < min_time_size:
        return dtw_with_input_prep(x, y, dist)

    reduced_x = reduce_array(x)
    reduced_y = reduce_array(y)
    distance, path = fastdtw(reduced_x, reduced_y, radius=radius, dist=dist)
    window = expand_window(path, len(x), len(y), radius)
    return dtw(x, y, window, dist)


def prep_inputs(x, y, dist):
    x = np.asanyarray(x, dtype='float')
    y = np.asanyarray(y, dtype='float')

    if dist is None:
        if x.ndim == 1:
            dist = difference
        else:
            dist = norm(p=1)
    elif isinstance(dist, numbers.Number):
        dist = norm(p=dist)

    return x, y, dist


def dtw_with_input_prep(x, y, dist=None):
    x, y, dist = prep_inputs(x, y, dist)
    return dtw(x, y, None, dist)


def dtw(x, y, window, dist):
    x_length, y_length = len(x), len(y)
    if window is None:
        window = [(i, j) for i in range(x_length) for j in range(y_length)]
    window = ((i + 1, j + 1) for i, j in window)
    D = defaultdict(lambda: (float('inf'),))
    D[0, 0] = (0.0, 0.0, 0.0)
    for i, j in window:
        dt = dist(x[i - 1], y[j - 1])
        D[i, j] = min((D[i - 1, j][0] + dt, i - 1, j), (D[i, j - 1][0] + dt, i, j - 1),
                      (D[i - 1, j - 1][0] + dt, i - 1, j - 1), key=lambda a: a[0])
    path = []
    i, j = x_length, y_length
    while not (i == j == 0):
        path.append((i - 1, j - 1))
        i, j = D[i, j][1], D[i, j][2]
    path.reverse()
    return (D[x_length, y_length][0], path)


def reduce_array(x):
    return [(x[i] + x[1 + i]) / 2 for i in range(0, len(x) - len(x) % 2, 2)]


def expand_window(path, len_x, len_y, radius):
    path_set = set(path)
    for i, j in path:
        for a, b in ((i + a, j + b)
                     for a in range(-radius, radius + 1)
                     for b in range(-radius, radius + 1)):
            path_set.add((a, b))

    window_ = set()
    for i, j in path_set:
        for a, b in ((i * 2, j * 2), (i * 2, j * 2 + 1),
                     (i * 2 + 1, j * 2), (i * 2 + 1, j * 2 + 1)):
            window_.add((a, b))

    window = []
    start_j = 0
    for i in range(0, len_x):
        new_start_j = None
        for j in range(start_j, len_y):
            if (i, j) in window_:
                window.append((i, j))
                if new_start_j is None:
                    new_start_j = j
            elif new_start_j is not None:
                break
        start_j = new_start_j

    return window


x = np.array([[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]])
y = np.array([[2, 2], [3, 3], [4, 4]])
distance, path = fastdtw_with_input_prep(x, y)
print(distance)
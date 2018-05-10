from __future__ import absolute_import, division
import numbers
import numpy
from collections import defaultdict


def custom_fastdtw(x, y, radius, distance_formula):
    x, y, distance_formula = prep_inputs(x, y, distance_formula)
    return fastdtw(x, y, radius, distance_formula)


def prep_inputs(x, y, distance_formula):
    x = numpy.asanyarray(x)
    y = numpy.asanyarray(y)

    if distance_formula is None:
        if x.ndim == 1:
            distance_formula = numerical_distance
        else:
            distance_formula = norm(1)
    elif isinstance(distance_formula, numbers.Number):
        distance_formula = norm(distance_formula)
    return x, y, distance_formula


def numerical_distance(a, b):
    return abs(a - b)


def norm(x):
    return lambda a, b: numpy.linalg.norm(a - b, x)


def fastdtw(x, y, radius, distance_formula):
    print(x)
    print(y)
    print(distance_formula(x, y))


custom_fastdtw([[1, 2], [2, 3]], [[4, 2], [2, 3]], 1, None)

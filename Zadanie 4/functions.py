import numpy as np


def quadratic_function(x: float) -> float:
    return x * x - 3 * x + 3


def trigonometric_function(x: float) -> float:
    return np.cos(x) * (x + 8)


def random_function(x: float) -> float:
    return 1/(x*x)


def function_value(x: float, flag: str) -> float:
    if flag == '1':
        return quadratic_function(x)
    elif flag == '2':
        return trigonometric_function(x)
    elif flag == '3':
        return random_function(x)

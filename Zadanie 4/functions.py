import numpy as np


def quadratic_function(x: float) -> float:
    return x ** 2 - 3 * x + 3


def trigonometric_function(x: float) -> float:
    return np.sin(x)


def logarithmic_function(x: float) -> float:
    return np.log(x + 3)


def mixed_function(x: float) -> float:
    return np.log(x + 2) - x ** 2 - np.sin(x)


def function_value(x: float, flag: str) -> float:
    if flag == '1':
        return quadratic_function(x)
    elif flag == '2':
        return trigonometric_function(x)
    elif flag == '3':
        return logarithmic_function(x)
    elif flag == '4':
        return mixed_function(x)

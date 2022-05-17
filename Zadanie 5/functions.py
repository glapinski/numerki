import numpy as np
import sympy as sp


def horner(x: float, parameters: list[float]) -> float:
    result = 0
    for i in parameters:
        result = result * x + i
    return result


def linear_function(x: float) -> float:
    return 3 * x - 5


def absolute_function(x: float) -> float:
    return abs(2 * x - 3)


def polynomial_function(x: float) -> float:
    return horner(x,  [1, -1, -1, -1, 1])


def trigonometric_function(x: float):
    if isinstance(x, float):
        return np.sin(x)
    return sp.sin(x)


def mixed_function(x: float):
    if isinstance(x, float):
        return np.cos(x) - x ** 3
    return sp.cos(x) - x ** 3


def function_value(x: float, flag: str) -> float:
    if flag == '1':
        return linear_function(x)
    elif flag == '2':
        return absolute_function(x)
    elif flag == '3':
        return polynomial_function(x)
    elif flag == '4':
        return trigonometric_function(x)
    elif flag == '5':
        return mixed_function(x)


def function_formula(flag: str):
    x = sp.Symbol('x')
    if flag == '1':
        return linear_function(x)
    elif flag == '2':
        return absolute_function(x)
    elif flag == '3':
        return polynomial_function(x)
    elif flag == '4':
        return trigonometric_function(x)

import numpy as np


def linear_function(x):
    return 5 * x - 2


def abs_function(x):
    return abs(x)


def horner(x, tab):
    result = 0
    for i in tab:
        result = result * x + i
    return result


def trigonometric_function(x):
    return np.sin(x)


def mixed_function(x):
    return np.abs(x ** 2 - 8 + np.cos(x))


def values(x, tab, flag):
    if flag == '1':
        return linear_function(x)
    elif flag == '2':
        return abs_function(x)
    elif flag == '3':
        return horner(x, tab)
    elif flag == '4':
        return trigonometric_function(x)
    else:
        return mixed_function(x)


def points(a, b, flag, arguments, calculated_values, tab):
    for i in np.arange(a, b, 0.01):
        arguments.append(i)
        calculated_values.append(values(i, tab, flag))


def interpolation(a, b, file_arguments, calculated_file_values, n, i_arguments, i_values):
    for i in np.arange(a, b, 0.01):
        y = 0.0
        for j in range(0, n):
            temp = np.double(calculated_file_values[j])
            for k in range(0, n):
                if j != k:
                    temp *= ((i - file_arguments[k]) / (file_arguments[j] - file_arguments[k]))
            y += temp
        i_arguments.append(i)
        i_values.append(y)
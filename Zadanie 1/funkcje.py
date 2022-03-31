import numpy as np
import sympy as sp


def horner(n, tab):
    result = 0
    for i in tab:
        result = result * n + i
    return result


def functionValue(a, b, flag):
    fa = function(a, flag)
    fb = function(b, flag)
    return fa, fb


def function(x, flag):
    fx = 0.0
    if flag == '1':
        parameters = [4, 3, 2, -1]
        fx = horner(x, parameters)
    if flag == '2':
        fx = 2 * np.sin(x) + np.cos(x)
    if flag == '3':
        fx = 7 ** x - 4
    if flag == '4':
        parameters = [1, 0, 0, 0]
        fx = horner(x, parameters) + 5**x - np.sin(x)
    return fx


def functionFormula(flag):
    arg_x = sp.Symbol('x')
    if flag == '1':
        parameters = [4, 3, 2, -1]
        fx = horner(arg_x, parameters)
    if flag == '2':
        fx = 2 * sp.sin(arg_x) + sp.cos(arg_x)
    if flag == '3':
        fx = 7 ** arg_x - 4
    if flag == '4':
        parameters = [1, 0, 0, 0]
        fx = horner(arg_x, parameters) + 5**arg_x - sp.sin(arg_x)
    return fx

from numpy import double

import funkcje as f
import sympy as sp


def styczneEps(a, b, eps, flag):
    iter = 0
    fa, fb = f.functionValue(a, b, flag)
    if fa * fb > 0:
        print("Funkcja nie spelnia zalozen (fa * fb > 0) ")
    else:
        df = sp.diff(f.functionFormula(flag))
        arg_x = sp.Symbol('x')
        current_x = a - double((f.function(a, flag) / df.subs(arg_x, a)))
        guardian = True
        while guardian is True:
            iter += 1
            if abs(f.function(current_x, flag)) < eps:
                return current_x, iter
            next_x = current_x - double((f.function(current_x, flag) / df.subs(arg_x, current_x)))
            current_x = next_x


def styczneIter(a, b, iter, flag):
    fa, fb = f.functionValue(a, b, flag)
    if fa * fb > 0:
        print("Funkcja nie spelnia zalozen (fa * fb >0) ")
    else:
        df = sp.diff(f.functionFormula(flag))
        arg_x = sp.Symbol('x')
        current_x = a - double((f.function(a, flag) / df.subs(arg_x, a)))
        while iter > 0:
            next_x = current_x - double((f.function(current_x, flag) / df.subs(arg_x, current_x)))
            current_x = next_x
            iter -= 1
        return current_x
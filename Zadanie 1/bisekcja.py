import funkcje as f


def bisekcjaEps(a, b, eps, flag):
    fa, fb = f.functionValue(a, b, flag)
    iter = 0
    if fa * fb > 0:
        print("Funkcja nie spelnia zalozen (fa * fb >0) ")
    else:
        guardian = True
        while guardian is True:
            iter += 1
            x0 = (a + b) / 2
            fx0 = f.function(x0, flag)
            if abs(fx0) < eps:
                return x0, iter
            if fx0 * fb < 0:
                a = x0
            else:
                b = x0
                fb = fx0


def bisekcjaIter(a, b, iter, flag):
    fa, fb = f.functionValue(a, b, flag)
    if fa * fb > 0:
        print("Funkcja nie spelnia zalozen (fa * fb >0) ")
    else:
        while iter > 0:
            x0 = (a + b) / 2
            fx0 = f.function(x0, flag)
            if fx0 == 0:
                return x0
            if fx0 * fb < 0:
                a = x0
            else:
                b = x0
                fb = fx0
            iter = iter - 1
        return x0
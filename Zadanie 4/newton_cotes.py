import functions as f


def simpson_formula(a: float, b: float, flag: str) -> float:
    quotient = (b - a) / 6.
    return quotient * (f.function_value(a, flag) + 4 * f.function_value((a + b) / 2, flag) + f.function_value(b, flag))


def newton_cotes_quadrature(a: float, b: float, flag: str, n: int) -> float:
    result = 0
    for i in range(n):
        h = (b - a) / n
        result += simpson_formula(a + i * h, a + h * (i + 1), flag)
    return result

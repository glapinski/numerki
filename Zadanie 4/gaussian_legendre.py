import numpy as np
import functions as f

legendre_polynomials_solutions = [
    [-np.sqrt(1 / 3), np.sqrt(1 / 3)],
    [-np.sqrt(3 / 5), 0, np.sqrt(3 / 5)],
    [-np.sqrt(3 / 7 + (2 / 7) * np.sqrt(6 / 5)), -np.sqrt(3 / 7 - (2 / 7) * np.sqrt(6 / 5)),
     np.sqrt(3 / 7 - (2 / 7) * np.sqrt(6 / 5)), np.sqrt(3 / 7 + (2 / 7) * np.sqrt(6 / 5))],
    [-1 / 3 * np.sqrt(5 + 2 * np.sqrt(10 / 7)), -1 / 3 * np.sqrt(5 - 2 * np.sqrt(10 / 7)), 0,
     1 / 3 * np.sqrt(5 - 2 * np.sqrt(10 / 7)), 1 / 3 * np.sqrt(5 + 2 * np.sqrt(10 / 7))]
]

gaussian_legendre_factors = [
    [1, 1],
    [5 / 9, 8 / 9, 5 / 9],
    [(18 - np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 + np.sqrt(30)) / 36, (18 - np.sqrt(30)) / 36],
    [(322 - 13 * np.sqrt(70)) / 900, (322 + 13 * np.sqrt(70)) / 900, 128 / 225,
     (322 + 13 * np.sqrt(70)) / 900, (322 - 13 * np.sqrt(70)) / 900]
]


def gaussian_legendre_quadrature(a: float, b: float, flag: str, node_count: int) -> float:
    result = 0.
    for i in range(node_count):
        t = ((a + b) / 2) + ((b - a) / 2) * legendre_polynomials_solutions[node_count - 2][i]
        result += ((b - a) / 2) * gaussian_legendre_factors[node_count - 2][i] * f.function_value(t, flag)
    return result

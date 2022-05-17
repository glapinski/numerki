import functions as f

legendre_polynomials_solutions = [
    [-0.577350269189625764509, 0.577350269189625764509],
    [-0.774596669241483377036, 0.000000000000000000000, 0.774596669241483377036],
    [-0.861136311594052575224, -0.339981043584856264803,
     0.339981043584856264803, 0.861136311594052575224],
    [-0.906179845938663992798, -0.538469310105683091036, 0.000000000000000000000,
     0.538469310105683091036, 0.906179845938663992798]
]

gaussian_legendre_factors = [
    [1.000000000000000000000, 1.000000000000000000000],
    [0.555555555555555555556, 0.888888888888888888889, 0.555555555555555555556],
    [0.347854845137453857373, 0.652145154862546142627, 0.652145154862546142627, 0.347854845137453857373],
    [0.236926885056189087514, 0.478628670499366468041, 0.568888888888888888889,
     0.478628670499366468041, 0.236926885056189087514]
]


def basic_function(x: float, k: int):
    p = [1, x]
    for i in range(2, k + 1):
        p.append(((2 * (i - 1) + 1) / i * x * p[i - 1] - (i - 1) / i * p[i - 2]))
    return p[k]


def calculate_numerator_for_coefficient(flag: str, node_count: int, k: int) -> float:
    integral = 0.
    for i in range(node_count):
        x = legendre_polynomials_solutions[node_count - 2][i]
        w = gaussian_legendre_factors[node_count - 2][i]
        integral += w * f.function_value(x, flag) * basic_function(x, k)
    return integral


def calculate_approximation_error(flag: str, k: int, coefficients, node_count: int) -> float:
    integral = 0.
    for i in range(node_count):
        x = legendre_polynomials_solutions[node_count - 2][i]
        w = gaussian_legendre_factors[node_count - 2][i]
        integral += w * (f.function_value(x, flag) - f.horner(x, get_approximation_coefficients(flag, node_count, k)))**2
    return integral


def calculate_approximation_coefficient(flag: str, node_count: int, k: int):
    return (2 * k + 1) / 2 * calculate_numerator_for_coefficient(flag, node_count, k)


def get_approximation_coefficients(flag: str, node_count: int, k: int):
    coefficients = []
    for i in range(k + 1):
        coefficients.append(calculate_approximation_coefficient(flag, node_count, i))
    return coefficients


def wart_wielomian(k, x, tab_wsp):
    """
    :param k: -//-
    :param x: -//-
    :param tab_wsp: -//-
    :return: wartość wielomianu aproksymującego dla argumentu x
    """
    poly = 0
    for i in range(k + 1):
        poly += tab_wsp[i] * basic_function(i, x)
    return poly

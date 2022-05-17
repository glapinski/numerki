import numpy as np
import matplotlib.pyplot as plt
import legendre_approximation as la
import functions as f


def main():
    chosen_function = input("Wybierz funkcje:\n"
                            "1. f(x) = 3x - 5\n"
                            "2. f(x) = |2x - 3|\n"
                            "3. f(x) = x^4 - x^3 - x^2 - x + 1\n"
                            "4. f(x) = sin(x)\n"
                            "5. f(x) = cos(x) - x^3\n")
    while not (chosen_function.isdigit() and ('1' <= chosen_function <= '5')):
        chosen_function = input("Niepoprawny wybor, spróbuj ponownie: ")
    input_a = float(input("Podaj poczatek przedziału a: "))
    input_b = float(input("Podaj koniec przedzialu b: "))
    while not (input_a < input_b):
        print("Początek przedziału musi być mniejszy niż koniec przedziału!")
        input_a = float(input("Podaj poczatek przedziału a: "))
        input_b = float(input("Podaj koniec przedzialu b: "))
    legendre_nodes = int(input("Podaj liczbę węzłów dla kwadratury Gaussa: "))
    while not 2 <= legendre_nodes <= 6:
        legendre_nodes = int(input("Liczba węzłów musi być liczbą całkowitą z przedziału [2;5]. Spróbuj ponownie: "))
    stop_condition = input("Wybierz kryterium aproksymacji:\n"
                           "1. Kryterium dokładności\n"
                           "2. Kryterium stopnia wielomianu aproksymującego")
    while not '1' <= stop_condition <= '2':
        stop_condition = input("Błędny wybór. Spróbuj ponownie: ")
    approximation_degree = 0
    chosen_degree = 0
    if stop_condition == '1':
        approximation_error = abs(float(input("Podaj oczekiwany maksymalny blad aproksymacji: ")))
        while not approximation_error != 0.0:
            approximation_error = abs(float(input("Niepoprawna wartość. Spróbuj ponownie: ")))
        approximation_degree = 1

        while not la.calculate_approximation_error(chosen_function, approximation_degree,
                                                   la.get_approximation_coefficients(chosen_function, legendre_nodes,
                                                                                     approximation_degree),
                                                   legendre_nodes) < approximation_error:
            approximation_degree += 1

    elif stop_condition == '2':
        chosen_degree = int(input("Podaj stopień wielomianu aproksymującego"))
        while not (chosen_degree >= 1):
            chosen_degree = int(input("Stopień wielomianu musi być liczbą całkowitą większą od 0! Spróbuj ponownie: "))
    arguments = np.linspace(input_a, input_b, 1000)
    values = []
    approximation_values = []
    approximation_polynomial_coefficients = []
    degree = 0
    if stop_condition == '1':
        approximation_polynomial_coefficients = la.get_approximation_coefficients(chosen_function, legendre_nodes, approximation_degree)
        degree = approximation_degree
    elif stop_condition == '2':
        approximation_polynomial_coefficients = la.get_approximation_coefficients(chosen_function, legendre_nodes, chosen_degree)
        degree = chosen_degree
    for i in arguments:
        values.append(f.function_value(i, chosen_function))
        approximation_values.append(f.horner(i, list(reversed(approximation_polynomial_coefficients))))

    plt.plot(arguments, values, label='Funkcja aproksymowana')
    plt.plot(arguments, la.polynomial_value(degree, arguments, approximation_polynomial_coefficients),
             label='Aproksymacja', linestyle=":")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Funkcja aproksymowana: " + str(f.function_formula(chosen_function)))
    plt.grid(True)
    plt.legend(loc="upper left")
    print("Wzór wielomianu aproksymacyjnego:\n")
    exponent = len(approximation_polynomial_coefficients) - 1
    polynomial_formula = ""
    for i in reversed(approximation_polynomial_coefficients):
        if i > 0.0 and exponent == len(approximation_polynomial_coefficients) - 1:
            polynomial_formula += str(i) + "x^" + str(exponent) + " "
        if i > 0.0 and exponent != len(approximation_polynomial_coefficients) - 1 and exponent != 0:
            polynomial_formula += "+ " + str(i) + "x^" + str(exponent) + " "
        if i < 0.0 and exponent != len(approximation_polynomial_coefficients) - 1 and exponent != 0:
            polynomial_formula += "- " + str(i) + "x^" + str(exponent) + " "
        if exponent == 0 and i > 0.0:
            polynomial_formula += "+ " + str(i)
        if exponent == 0 and i < 0.0:
            polynomial_formula += "- " + str(i)
        exponent -= 1
    print(polynomial_formula)
    print(f"Bład aproksymacji: {la.calculate_approximation_error(chosen_function, degree, approximation_polynomial_coefficients, legendre_nodes)}")
    plt.show()


if __name__ == '__main__':
    main()

import newton_cotes as nc
import gaussian_legendre as gl

def main():
    chosen_function = input("Wybierz funkcje:\n"
                            "1 - Kwadratowa: x^2 - 3x + 3\n"
                            "2 - Trygonometryczna: sin(x)\n"
                            "3 - Logarytmiczna: log(x + 3)\n"
                            "4 - Złożona: log(x+2) - x^2 - sin(x): ")
    while not (chosen_function.isdigit() or '1' <= chosen_function <= '4'):
        chosen_function = input("Niepoprawny wybor, spróbuj ponownie: ")
    input_a = float(input("Podaj poczatek przedziału a: "))
    input_b = float(input("Podaj koniec przedzialu b: "))
    while not (input_a < input_b):
        print("Początek przedziału musi być mniejszy niż koniec przedziału!")
        input_a = float(input("Podaj poczatek przedziału a: "))
        input_b = float(input("Podaj koniec przedzialu b: "))
    input_epsilon = float(input("Podaj epsilon e: "))
    iterations = 1
    previous_result_nc = 0
    result_nc = nc.newton_cotes_quadrature(input_a, input_b, chosen_function, iterations)
    while result_nc - previous_result_nc > input_epsilon:
        iterations += 1
        previous_result_nc = result_nc
        result_nc = nc.newton_cotes_quadrature(input_a, input_b, chosen_function, iterations)
    print(f"Wynik dla złożonej kwadratury Newtona-Cotesa: {round(result_nc, 5)}   Liczba przebiegów: {iterations}")
    for i in range(2, 6):
        result_gl = gl.gaussian_legendre_quadrature(input_a, input_b, chosen_function, i)
        print(f"Wynik dla kwadratura Gaussa-Legendre'a: {round(result_gl, 5)}   Liczba węzłów: {i}")


if __name__ == '__main__':
    main()

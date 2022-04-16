import numpy as np
import functions as f
import graphs as g


def main():
    a = 0.0
    b = 0.0
    parameters = [1, 5, -4, -20]
    arguments = []
    values = []
    print("Program interpoluje dana funkcje metoda Lagrange'a dla nierownych odstepow argumentu. \n"
          "Dane pobierane sa z pliku nodes.txt.")
    choose = input("Wybierz funkcje: \n "
                   "1. Funkcja liniowa y=5x-2 \n "
                   "2. Funkcja modul z x y=|x| \n "
                   "3. Wielomian y=x^3+5x^2-4x-20 \n "
                   "4. Funkcja trygonometryczna y=sin(x) \n "
                   "5. Zlozenie funkcji y=|x^2-8+cos(x)|")
    if 1 <= int(choose) <= 5:
        print("Okresl przedzial")
        a = np.double(input("Podaj a: "))
        b = np.double(input("Podaj b: "))
    else:
        print("Nie ma takiej funkcji")
        exit()

    f.points(a, b, choose, arguments, values, parameters)
    file_arguments = np.loadtxt("nodes.txt", dtype='d', delimiter='\n')
    calculated_file_values = f.values(file_arguments, parameters, choose)
    i_arguments = []
    i_values = []
    f.interpolation(a, b, file_arguments, calculated_file_values, len(file_arguments), i_arguments, i_values)
    g.graph(a, b, arguments, values, file_arguments, calculated_file_values, i_arguments, i_values)


if __name__ == '__main__':
    main()

from numpy import double

import bisekcja
import graphs
import styczne


def main():
    choose = input("Wybierz wariant funkcji:\n1. Wielomianowa\n2. Trygonometryczna\n3. Wykladnicza\n4. Zlozona\n")
    metoda = input("Wybierz metode:\n1. Bisekcja\n2. Siecznych\n")

    check = False
    while not check:
        a = double(input("Wartosc lewego przedzialu: "))
        b = double(input("Wartosc prawego przedzialu: "))
        if a <= b:
            check = True
        if not check:
            print("Wartosc lewego przedzialu musi byc mniejsza niz wartosc prawego przedzialu!\n")

    ending = input("Podaj warunek zakonczenia: \n1 - dokladnosc obliczen\n2 - podanie liczby iteracji: ")
    if ending == '1':
        eps = double(input('Podaj eps: '))
        print("Wynik wynosi: ")
        if metoda == '1':
            print(str(bisekcja.bisekcjaEps(a, b, eps, choose)[0]) + "\nIlosc iteracji: \n" +
                  str(bisekcja.bisekcjaEps(a, b, eps, choose)[1]))
            graphs.graph(a, b, bisekcja.bisekcjaEps(a, b, eps, choose)[0], choose)
        if metoda == '2':
            print(str(styczne.styczneEps(a, b, eps, choose)[0]) + "\nIlosc iteracji: \n" +
                  str(styczne.styczneEps(a, b, eps, choose)[1]))
            graphs.graph(a, b, styczne.styczneEps(a, b, eps, choose)[0], choose)

    if ending == '2':
        iter = int(input("Podaj ilosc iteracji: "))
        print("Wynik wynosi: ")
        if metoda == '1':
            print(str(bisekcja.bisekcjaIter(a, b, iter, choose)))
            graphs.graph(a, b, bisekcja.bisekcjaIter(a, b, iter, choose), choose)
        if metoda == '2':
            print(str(styczne.styczneIter(a, b, iter, choose)))
            graphs.graph(a, b, styczne.styczneIter(a, b, iter, choose), choose)


if __name__ == '__main__':
    main()

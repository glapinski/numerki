eps = 0.000000001


def switch_rows(matrix, row1, row2):
    for i in range(len(matrix) + 1):
        matrix[row1][i], matrix[row2][i] = matrix[row2][i], matrix[row1][i]


def sort_to_triangle(matrix):
    for i in range(len(matrix) - 1):
        if abs(matrix[i][i]) < eps:
            for j in range(i + 1, len(matrix)):
                if abs(matrix[j][i]) > eps:
                    print(matrix)
                    switch_rows(matrix, i, j)
                    print(matrix)


def elimination(matrix):
    for i in range(len(matrix) - 1):
        sort_to_triangle(matrix)
        if abs(matrix[i][i]) < eps:
            print("Blad: blad w elimination()")
            return False
        for j in range(i + 1, len(matrix)):
            m = -matrix[j][i] / matrix[i][i]
            for k in range(i, len(matrix) + 1):
                matrix[j][k] += m * matrix[i][k]
    return True


def find(matrix):
    X = []
    X = [0 for i in range(len(matrix))]
    for i in range(len(matrix) - 1, -1, -1):
        if abs(matrix[i][i]) < eps:
            if abs(matrix[i][i + 1]) < eps:
                print("Podany uklad jest ukladem nieoznaczonym.")
            else:
                print("Podany uklad jest ukladem sprzecznym.")
            return False
        s = matrix[i][len(matrix)]
        for j in range(len(matrix) - 1, i, -1):
            s -= matrix[i][j] * X[j]
        X[i] = s / matrix[i][i]
    return X


def calculate(matrix):
    if elimination(matrix) and find(matrix):
        print("Rozwiazaniem jest: ")
        for i in range(len(matrix)):
            print("x" + str(i + 1) + " = " + str(find(matrix)[i]) + "\n")
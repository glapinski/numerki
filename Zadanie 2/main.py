import files as f
import gauss as g


def main():
    matrix_a = f.matrix_from_file("matrixa.txt")
    matrix_b = f.matrix_from_file("matrixb.txt")
    matrix_c = f.matrix_from_file("matrixc.txt")
    matrix_d = f.matrix_from_file("matrixd.txt")
    matrix_e = f.matrix_from_file("matrixe.txt")
    matrix_f = f.matrix_from_file("matrixf.txt")
    matrix_g = f.matrix_from_file("matrixg.txt")
    matrix_h = f.matrix_from_file("matrixh.txt")
    matrix_i = f.matrix_from_file("matrixi.txt")
    matrix_j = f.matrix_from_file("matrixj.txt")
    matrix_user = f.matrix_from_file("matrixuser.txt")
    g.calculate(matrix_user)


if __name__ == '__main__':
    main()


import numpy as np


def matrix_from_file(path):
    matrix_ab = np.loadtxt(path, dtype='d', delimiter=' ')
    return matrix_ab

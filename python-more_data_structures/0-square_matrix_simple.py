#!/usr/bin/python3
def square(i):
    product = i * i
    return product


def square_matrix_simple(matrix=[]):
    new_matrix = matrix[:][:]

    for i in range(len(matrix)):
        new_matrix.append(list(map(square, matrix[i])))
    return new_matrx

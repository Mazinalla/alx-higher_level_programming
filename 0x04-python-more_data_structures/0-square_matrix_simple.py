#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix using map.

    :param matrix: A 2D matrix (list of lists) containing integers.
    :type matrix: list of lists
    :return: A new matrix with the square values of the original integers.
    :rtype: list of lists
    """
    def square_row(row):
        return list(map(lambda x: x ** 2, row))

    return list(map(square_row, matrix))

#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        # Create a formatted string for each row, using str.format() for each element
        print(" ".join("{:d}".format(element) for element in row))

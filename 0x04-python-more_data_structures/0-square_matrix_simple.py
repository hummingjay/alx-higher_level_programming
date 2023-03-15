#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if not matrix:
        return matrix
    else:
        for row in matrix:
            for element in row:
               new_row.(element**2)
            new_matrix.append(new_row)
    return new_matrix

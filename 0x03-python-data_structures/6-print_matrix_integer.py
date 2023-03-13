#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return matrix
    else:
        for row in matrix:
            for char in row:
                print("{:}".format(char), end='')
                # this above will print each element
            print()
            # this will print out each row

#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    reloaded = matrix.copy()
    reloaded = [[x**2 for x in row] for row in reloaded]
    return reloaded

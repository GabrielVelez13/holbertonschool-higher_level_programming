#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for line in matrix:
        print(" ".join(map(str, line)))

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

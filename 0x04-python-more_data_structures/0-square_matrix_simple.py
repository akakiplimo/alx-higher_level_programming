#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
 """Compute square of all individual elements in a matrix"""
 return list(list(map(lambda x: x * x, row)) for row in matrix)

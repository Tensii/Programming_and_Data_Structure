#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div.
    Args:
        matrix: list of lists of integers/floats
        div: number to divide by
    Returns:
        New matrix with all elements divided by div
    Raises:
        TypeError: If matrix is not list of lists of numbers or rows have different sizes
        ZeroDivisionError: If div is 0
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    row_size = len(matrix[0]) if matrix else 0
    if not all(len(row) == row_size for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    
    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    return [[round(num / div, 2) for num in row] for row in matrix]

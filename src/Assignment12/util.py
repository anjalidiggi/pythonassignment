# util.py :- This file will contain the function for validating problem statement
import numpy as np


def calculate_determinant(matrix):
    matrix = np.array(matrix)
    determinant = np.linalg.det(matrix)
    return round(determinant, 2)

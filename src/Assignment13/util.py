# util.py :- This file will contain the function for validating problem statement
import numpy as np

def calculate_mean_var_std(matrix):
    matrix = np.array(matrix)
    mean = np.mean(matrix, axis=1)
    var = np.var(matrix, axis=0)
    std = np.std(matrix)
    return mean, var, std

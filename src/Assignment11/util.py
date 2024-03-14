# util.py :- This file will contain the function for validating problem statement
import numpy as np

def find_max_of_min(arr):
    arr = np.array(arr)
    min_values = np.min(arr, axis=1)
    max_of_min = np.max(min_values)
    return max_of_min

# util.py :- This file will contain the function to process array in floor ,ceil and rint
import numpy as np


def process_array(input_str):
    # Convert the input string to a numpy array
    array = np.array(input_str.split(), dtype=float)

    # Apply floor, ceil, and rint functions to the array
    floor_array = np.floor(array)
    ceil_array = np.ceil(array)
    rint_array = np.rint(array)

    return floor_array, ceil_array, rint_array

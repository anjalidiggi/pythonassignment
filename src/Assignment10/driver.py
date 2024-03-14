"""
Problem Statement : -
You are given a 1-D array, . Your task is to print the floor ,ceil  and rint of all the elements of .

Note
In order to get the correct output format, add the line numpy.set_printoptions(legacy='1.13') below the numpy import.

Input Format

A single line of input containing the space separated elements of array A.

Output Format

On the first line, print floor the  of A.
On the second line, print ceil the  of A.
On the third line, print the rint  of A.
"""
"""
Sample Output :-
input:-Enter the space-separated elements of array A: 1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
output
Floor of A:
[1. 2. 3. 4. 5. 6. 7. 8. 9.]

Ceil of A:
[ 2.  3.  4.  5.  6.  7.  8.  9. 10.]

Rint of A:
[ 1.  2.  3.  4.  6.  7.  8.  9. 10.]


"""

# driver.py :This file will prompt the user to Enter the space-separated elements of array A and
# # then call the function process_array
# from util.py to get value in floor,ceil and rint.

import numpy as np
from util import process_array


def main():
    # Input
    input_str = input("Enter the space-separated elements of array A: ")

    # Process the array
    floor_array, ceil_array, rint_array = process_array(input_str)

    # Output
    print("Floor of A:")
    print(floor_array)
    print("\nCeil of A:")
    print(ceil_array)
    print("\nRint of A:")
    print(rint_array)


if __name__ == "__main__":
    main()

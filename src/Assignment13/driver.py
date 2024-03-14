"""
Problem Statement : -
Task

You are given a 2-D array of size N * M.
Your task is to find:

The mean along axis 1.
The var along axis  0.
The std along axis None
Input Format

The first line contains the space separated values of N and M.
The next N  lines contains M  space separated integers.

Output Format

First, print the mean.
Second, print the var.
Third, print the std.
"""
"""
Sample Output :-
Enter the size of the 2D array (N M): 2 2
Enter the elements of the 2D array:
1 2 
3 4
Mean along axis 1: [1.5 3.5]
Var along axis 0: [1. 1.]
Std along axis None: 1.118033988749895

"""
# driver.py :This file will prompt the user to Enter the size of the 2D array (N M):  and
#  and Enter the elements of the 2D array: then call the function calculate_mean_var_std
# from util.py to get value of Mean,Var and Std:"

from util import calculate_mean_var_std


def main():
    N, M = map(int, input("Enter the size of the 2D array (N M): ").split())
    print("Enter the elements of the 2D array:")
    matrix = []
    for _ in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    mean, var, std = calculate_mean_var_std(matrix)
    print("Mean along axis 1:", mean)
    print("Var along axis 0:", var)
    print("Std along axis None:", std)


if __name__ == "__main__":
    main()

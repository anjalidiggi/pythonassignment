"""
Problem Statement : -
Task

You are given a 2-D array with dimensions N*M.
Your task is to perform the min function over axis 1  and then find the max of that.

Input Format

The first line of input contains the space separated values of  N and M.
The next N  lines contains M  space separated integers.

Output Format

Compute the min along axis 1 and then print the max of that result.
"""
"""
Sample Output :-

Enter the dimensions of the 2-D array (N M): 4 2
Enter the elements of the 2-D array:
2 5
2 7
1 3
4 0
Max of min values along axis 1: 2
"""
# driver.py :This file will prompt the user to Enter the dimensions of the 2-D array (N M):  and
# and Enter the elements of the 2-D array: then call the function find_max_of_min
# from util.py to "Max of min values along axis 1:"
from util import find_max_of_min


def main():
    N, M = map(int, input("Enter the dimensions of the 2-D array (N M): ").split())
    arr = []
    print("Enter the elements of the 2-D array:")
    for _ in range(N):
        row = list(map(int, input().split()))
        arr.append(row)

    max_of_min = find_max_of_min(arr)
    print("Max of min values along axis 1:", max_of_min)


if __name__ == "__main__":
    main()

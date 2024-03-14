"""
Problem Statement : -
Task

You are given a square matrix  with dimensions N*N. Your task is to find the determinant. Note: Round the answer to 2 places after the decimal.

Input Format

The first line contains the integer .
The next  lines contains the  space separated elements of array .

Output Format

Print the determinant of A .
"""
"""
Sample Output :-
Enter the size of the square matrix: 2
Enter the elements of the square matrix:
1.1 1.1
1.1 1.1
Determinant: 0.0

"""
# driver.py :This file will prompt the user to Enter the size of the square matrix:   and
#  then call the function calculate_determinant
# from util.py to get value of Determinant:"
from util import calculate_determinant


def main():
    N = int(input("Enter the size of the square matrix: "))
    print("Enter the elements of the square matrix:")
    matrix = []
    for _ in range(N):
        row = list(map(float, input().split()))
        matrix.append(row)

    determinant = calculate_determinant(matrix)
    print("Determinant:", determinant)


if __name__ == "__main__":
    main()

"""
Problem Statement : -
There is a horizontal row of n cubes. The length of each cube is given.
 You need to create a new vertical pile of cubes.
 The new pile should follow these directions: if  is on top of  then .

When stacking the cubes, you can only pick up either the leftmost or the rightmost cube
each time. Print Yes if it is possible to stack the cubes. Otherwise, print No.
"""
"""
Sample Output :-
input :-
Enter the number of test cases: 2
6
4 3 2 1 3 4
output:-

Yes
input:-
3
1 3 2
No
"""
# driver.py :This file will prompt the user to Enter the number of test cases:
#  then call the function can_stack_cubes
# from util.py to Print Yes if it is possible to stack the cubes. Otherwise, print No.

from util import can_stack_cubes


def main():
    t = int(input("Enter the number of test cases: "))
    for _ in range(t):
        n = int(input())
        cubes = list(map(int, input().split()))
        if can_stack_cubes(n, cubes):
            print("Yes")
        else:
            print("No")


if __name__ == "__main__":
    main()

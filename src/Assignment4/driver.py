
"""
Write a Python program for below problem statement:

Function Description

Complete the merge_the_tools function in the editor below.

merge_the_tools has the following parameters:

string s: the string to analyze
int k: the size of substrings to analyze
Prints

Print each subsequence on a new line. There will be  of them. No return value is expected.

Sample output :-
Enter the string: AABCAAADA
Enter the size of substrings: 3
AB
CA
AD

"""
# driver.py: This file will call the merge_the_tools function from util.py.
from util import merge_the_tools

def main():
    # Input string
    s = input("Enter the string: ")

    # Input size of substrings
    k = int(input("Enter the size of substrings: "))

    # Merge the tools
    merge_the_tools(s, k)


if __name__ == "__main__":
    main()

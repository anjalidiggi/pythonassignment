
"""
Write a Python program for below problem statement

Problem Statement :---
Problem Statement : -
Task

You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (__) with rjust, ljust or center.

Input Format

A single line containing the thickness value for the logo.

"""
"""
Sample Output :-
Enter the thickness of the HackerRank Logo: 2
Enter the character to use in the logo: H
 H 
HHH
 HH      HH     
 HH      HH     
 HH      HH     
 HHHHHHHHHH 
 HH      HH     
 HH      HH     
 HH      HH     
        HHH 
         H  
"""
# driver.py :- This file will call the print_hackerrank_logo function from util.py.
from util import print_hackerrank_logo


def main():
    # Input thickness of the HackerRank Logo
    thickness = int(input("Enter the thickness of the HackerRank Logo: "))

    # Input character to use in the logo
    character = input("Enter the character to use in the logo: ")

    # Print the HackerRank Logo
    print_hackerrank_logo(thickness, character)


if __name__ == "__main__":
    main()

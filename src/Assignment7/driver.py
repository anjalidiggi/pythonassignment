"""
Problem Statement : -
Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in    format.

Constraints

Output Format

Output the correct day in capital letters.
"""
"""
Sample Output :-
Enter the date in format (month day year): 01 22 2024
Day: MONDAY
"""

# driver.py :- This file will prompt the user to enter a date and
# then call the find_day function from util.py to determine the day.

from util import find_day


def main():
    # Input the date in the format (month day year)
    month, day, year = map(int, input("Enter the date in format (month day year): ").split())

    # Find the day corresponding to the date
    day_of_week = find_day(month, day, year)

    # Print the day
    print("Day:", day_of_week)


if __name__ == "__main__":
    main()

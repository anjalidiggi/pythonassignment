"""
Write a Python program to find the runner-up score
Problem statement:

Given the participants' score sheet for your university sports day
You are required to find the runner-up score. You are given scores.
. Store them in a list and find the score of the runner-up score
Sample output :-
Enter scores separated by space: 5 4 9 2 8 1 6
Runner-up score: 8
"""

# driver.py : This file will call the find_runner_up function from util.py.
from util import find_runner_up


def main():
    # Input scores
    scores = [int(x) for x in input("Enter scores separated by space: ").split()]

    # Find the runner-up score
    runner_up_score = find_runner_up(scores)

    print("Runner-up score:", runner_up_score)

if __name__ == "__main__":
    main()

# util.py :- This file will contain the function for validating problem statement
def calculate_happiness(n, m, arr, A, B):
    happiness = 0
    for num in arr:
        if num in A:
            happiness += 1
        elif num in B:
            happiness -= 1
    return happiness

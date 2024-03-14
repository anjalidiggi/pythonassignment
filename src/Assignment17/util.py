# util.py :- This file will contain the function for validating problem statement
from itertools import combinations


def probability_of_letter_present(N, letters, K):
    total_combinations = list(combinations(range(N), K))
    count = sum(1 for indices in total_combinations if 'a' in [letters[i] for i in indices])
    return count / len(total_combinations)

"""
Problem Statement : -
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination. Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

To read more about the functions in this module, check out their documentation here.

You are given a list of N lowercase English letters. For a given integer N, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: ''.

"""
"""
Sample Output :-
input:-
Enter the count of lowercase letters: 4
Enter the lowercase letters separated by space: a a c d 
Enter the value of K: 2
output :- 

Probability of at least one 'a' in 2 indices: 0.8333

"""
# driver.py :This file will prompt the user to Enter the count of lowercase letters:
#  and Enter the lowercase letters separated by space:
#  and Enter the value of K: then call the function probability_of_letter_present
# from util.py to Find the probability that at least one of the K indices selected will contain the letter: 'a'.
from util import probability_of_letter_present


def main():
    N = int(input("Enter the count of lowercase letters: "))
    letters = input("Enter the lowercase letters separated by space: ").split()
    K = int(input("Enter the value of K: "))
    probability = probability_of_letter_present(N, letters, K)
    print(f"Probability of at least one 'a' in {K} indices: {probability:.4f}")


if __name__ == "__main__":
    main()

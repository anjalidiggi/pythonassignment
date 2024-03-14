"""
Problem Statement : -
You are given n words. Some words may repeat.
 For each word, output its number of occurrences.
  The output order should correspond with the input order of appearance of the word.
   See the sample input/output for clarification.

Note: Each input line ends with a "\n" character.
"""
"""
Sample Output :-
input :-
4
bcdef
abcdefg
bcde
bcdef

output:-
2
1
1
2

"""
# driver.py :This file will prompt the user to Enter number of words count and all words
#  then call the function count_word_occurrences
# from util.py to word order"
from util import count_word_occurrences


def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    occurrences = count_word_occurrences(n, words)
    for count in occurrences:
        print(count)


if __name__ == "__main__":
    main()

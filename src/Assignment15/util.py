# util.py :- This file will contain the function for validating problem statement
def count_word_occurrences(n, words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return [word_count[word] for word in words]


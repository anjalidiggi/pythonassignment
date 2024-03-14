# test_case.py :-This file will contain unit tests
# to validate the count_word_occurrences function in util.py
#  It counts the occurrences of words and maintains the order of appearance.
#  The unit tests validate the correctness of the solution.
import unittest
from src.Assignment15.util import count_word_occurrences


class TestCountWordOccurrences(unittest.TestCase):
    def test_count_word_occurrences(self):
        occurrences1 = count_word_occurrences(4, ['bcdef', 'abcdefg', 'bcde', 'bcdef'])
        self.assertEqual(occurrences1, [2, 1, 1, 2])

        occurrences2 = count_word_occurrences(5, ['apple', 'banana', 'apple', 'orange', 'banana'])
        self.assertEqual(occurrences2, [2, 2, 2, 1, 2])

        occurrences3 = count_word_occurrences(3, ['a', 'a', 'b'])
        self.assertEqual(occurrences3, [2, 2, 1])


if __name__ == '__main__':
    unittest.main()

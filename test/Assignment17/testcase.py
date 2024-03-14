# test_case.py :-This file will contain unit tests
# to validate the probability_of_letter_present function in util.py
#   It calculates the probability of selecting at least one index
#   containing the letter 'a' when choosing K indices from a list of lowercase letters.
#  The unit tests validate the correctness of the solution.
import unittest
from src.Assignment17.util import probability_of_letter_present


class TestProbabilityOfLetterPresent(unittest.TestCase):
    def test_probability_of_letter_present(self):
        self.assertAlmostEqual(probability_of_letter_present(4, ['a', 'a', 'c', 'd'], 2), 0.8333, places=4)
        self.assertAlmostEqual(probability_of_letter_present(5, ['a', 'b', 'c', 'd', 'e'], 3), 0.6, places=4)
        self.assertAlmostEqual(probability_of_letter_present(3, ['a', 'a', 'a'], 1), 1.0000, places=4)


if __name__ == '__main__':
    unittest.main()

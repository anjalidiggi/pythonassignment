# test_case.py :-This file will contain unit tests
# to validate the calculate_happiness function in util.py
# It calculates the total happiness based on the given conditions
# and validates the correctness of the solution using unit tests.
import unittest
from src.Assignment14.util import calculate_happiness


class TestCalculateHappiness(unittest.TestCase):
    def test_calculate_happiness(self):
        happiness1 = calculate_happiness(3, 2, [1, 5, 3], {3, 1}, {5, 7})
        self.assertEqual(happiness1, 1)

        happiness2 = calculate_happiness(5, 3, [10, 20, 30, 40, 50], {10, 30, 50}, {20, 40})
        self.assertEqual(happiness2, 1)

        happiness3 = calculate_happiness(4, 2, [7, 8, 9, 10], {7, 9}, {8, 10})
        self.assertEqual(happiness3, 0)


if __name__ == '__main__':
    unittest.main()

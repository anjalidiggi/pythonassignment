# test_case.py :-This file will contain unit tests
# to validate the def calculate_determinant(matrix): function in util.py.

import unittest
from src.Assignment12.util import calculate_determinant


class TestCalculateDeterminant(unittest.TestCase):
    def test_calculate_determinant(self):
        matrix1 = [[1.1, 1.1], [1.1, 1.1]]
        self.assertEqual(calculate_determinant(matrix1), 0.0)

        matrix2 = [[2, 0], [0, 2]]
        self.assertEqual(calculate_determinant(matrix2), 4.0)

        matrix3 = [[3, 1], [1, 3]]
        self.assertEqual(calculate_determinant(matrix3), 8.0)


if __name__ == '__main__':
    unittest.main()

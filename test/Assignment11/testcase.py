# test_case.py :-This file will contain unit tests
# to validate the find_max_of_min function in util.py.
import unittest
from src.Assignment11.util import find_max_of_min


class TestFindMaxOfMin(unittest.TestCase):
    def test_find_max_of_min(self):
        arr1 = [[2, 5], [2, 7], [1, 3], [4, 0]]
        self.assertEqual(find_max_of_min(arr1), 2)

        arr2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(find_max_of_min(arr2), 7)

        arr3 = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
        self.assertEqual(find_max_of_min(arr3), 70)


if __name__ == '__main__':
    unittest.main()

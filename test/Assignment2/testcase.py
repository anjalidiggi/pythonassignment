# test_case.py
import unittest
from src.Assignment2.util import find_runner_up


class TestFindRunnerUpScore(unittest.TestCase):
    def test_find_runner_up(self):
        # Test case with three different inputs
        self.assertEqual(find_runner_up([2, 3, 6, 6, 5]), 5)
        self.assertEqual(find_runner_up([1, 1, 1, 1, 1]), 1)
        self.assertEqual(find_runner_up([1, 2, 3, 4, 5]), 4)

    def test_empty_list(self):
        # Test case with an empty list of scores
        self.assertIsNone(find_runner_up([]))


if __name__ == "__main__":
    unittest.main()

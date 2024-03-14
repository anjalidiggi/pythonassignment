# test_case.py :-This file will contain unit tests to validate the mutate_string function in util.py.
# test_case.py
import unittest
from src.Assignment3.util import mutate_string_with_list, mutate_string_with_slice


class TestMutateString(unittest.TestCase):
    def test_mutate_string_with_list(self):
        # Test case with three different inputs
        self.assertEqual(mutate_string_with_list("abcdef", 2, "x"), "abxdef")
        self.assertEqual(mutate_string_with_list("hello", 0, "H"), "Hello")
        self.assertEqual(mutate_string_with_list("python", 4, "X"), "pythXn")

    def test_mutate_string_with_slice(self):
        # Test case with three different inputs
        self.assertEqual(mutate_string_with_slice("abcdef", 2, "x"), "abxdef")
        self.assertEqual(mutate_string_with_slice("hello", 0, "H"), "Hello")
        self.assertEqual(mutate_string_with_slice("python", 4, "X"), "pythXn")


if __name__ == "__main__":
    unittest.main()

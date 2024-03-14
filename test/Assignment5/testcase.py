# test_case.py: This file will contain unit tests to validate the print_formatted function in util.py.
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.Assignment5.util import print_formatted


class TestStringFormattingProblem(unittest.TestCase):
    def test_print_formatted(self):
        # Test case with three different inputs
        n1 = 5
        expected_output1 = "  1   1   1   1\n  2   2   2  10\n  3   3   3  11\n  4   4   4 100\n  5   5   5 101\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            print_formatted(n1)
            self.assertEqual(buffer.getvalue(), expected_output1)

        n2 = 6
        expected_output2 = "  1   1   1   1\n  2   2   2  10\n  3   3   3  11\n  4   4   4 100\n  5   5   5 101\n  6   6   6 110\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            print_formatted(n2)
            self.assertEqual(buffer.getvalue(), expected_output2)

        n3 = 2
        expected_output3 =" 1  1  1  1\n 2  2  2 10\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            print_formatted(n3)
            self.assertEqual(buffer.getvalue(), expected_output3)


if __name__ == "__main__":
    unittest.main()

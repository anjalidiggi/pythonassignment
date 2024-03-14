# test_case.py: This file will contain unit tests to validate the merge_the_tools function in util.py.

import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.Assignment4.util import merge_the_tools


class TestMergetheToolsProblem(unittest.TestCase):
    def test_merge_the_tools(self):
        # Test case with three different inputs
        s1 = "AABCAAADA"
        k1 = 3
        expected_output1 = "AB\nCA\nAD\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            merge_the_tools(s1, k1)
            self.assertEqual(buffer.getvalue(), expected_output1)

        s2 = "ABCDEF"
        k2 = 2
        expected_output2 = "AB\nCD\nEF\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            merge_the_tools(s2, k2)
            self.assertEqual(buffer.getvalue(), expected_output2)

        s3 = "AAABBBCCCDDDEEE"
        k3 = 4
        expected_output3 = "AB\nBC\nCD\nE\n"
        with StringIO() as buffer, redirect_stdout(buffer):
            merge_the_tools(s3, k3)
            self.assertEqual(buffer.getvalue(), expected_output3)


if __name__ == "__main__":
    unittest.main()

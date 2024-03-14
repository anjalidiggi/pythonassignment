# test_case.py
import unittest
from io import StringIO
from contextlib import redirect_stdout
from src.Assignment6.util import print_hackerrank_logo


class ValidateTextAlignmentProblem(unittest.TestCase):
    def test_print_hackerrank_logo(self):
        # Test case with thickness 1 and character 'H'
        thickness1 = 1
        character1 = 'H'
        expected_output1 = "H\nH   H   \nH   H   \nHHHHH \nH   H   \nH   H   \n    H \n"
        with StringIO() as buffer, redirect_stdout(buffer):
            print_hackerrank_logo(thickness1, character1)
            self.assertEqual(buffer.getvalue(), expected_output1)

    if __name__ == "__main__":
        unittest.main()

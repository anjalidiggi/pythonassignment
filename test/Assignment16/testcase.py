# test_case.py :-This file will contain unit tests
# to validate the can_stack_cubes function in util.py
#  It countsIt determines whether it is possible to stack the cubes according to the given conditions.
#  The unit tests validate the correctness of the solution.
import unittest
from src.Assignment16.util import can_stack_cubes


class TestCanStackCubes(unittest.TestCase):
    def test_can_stack_cubes(self):
        self.assertTrue(can_stack_cubes(6, [4, 3, 2, 1, 3, 4]))
        self.assertFalse(can_stack_cubes(3, [1, 3, 2]))
        self.assertFalse(can_stack_cubes(5, [3, 4, 5, 4, 3]))


if __name__ == '__main__':
    unittest.main()

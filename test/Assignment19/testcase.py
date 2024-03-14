# test_case.py :-This file will contain unit tests
# to validate the extract_valid_emails function in util.py
# The execute_commands function interprets and executes the given commands on the list.
#  The unit tests validate the correctness of the solution.
import unittest
from src.Assignment19.util import execute_commands


class TestPythonListExecuteCommands(unittest.TestCase):
    def test_execute_commands(self):
        commands1 = ['insert 0 5', 'insert 1 10', 'insert 0 6', 'print']
        self.assertEqual(execute_commands(commands1), [6, 5, 10])

        commands2 = ['append 1', 'append 2', 'append 3', 'print']
        self.assertEqual(execute_commands(commands2), [1, 2, 3])

        commands3 = ['insert 0 3','remove 3', 'append 4', 'append 5', 'print']
        self.assertEqual(execute_commands(commands3), [4, 5])


if __name__ == '__main__':
    unittest.main()

# test_case.py :-This file will contain unit tests
# to validate the calculate_average_marks function in util.py.

import unittest
from src.Assignment8.util import calculate_average_marks


class TestUtilFunctions(unittest.TestCase):
    def test_calculate_average_marks(self):
        # Test case with 2 students
        students1 = [['ID', 'MARKS', 'NAME', 'CLASS'],
                     ['1', '97', 'ANJALI', '9'],
                     ['2', '87', 'GAYTRI', '8']]
        expected_output1 = 92.00
        self.assertEqual(calculate_average_marks(students1), expected_output1)

        # Test case with 3 students
        students2 = [['MARKS', 'ID', 'NAME', 'CLASS'],
                     ['89', '1', 'ANJALISAWLA', '7'],
                     ['77', '2', 'MOTI', '8'],
                     ['91', '3', 'ANJALIGUPTA', '9']]
        expected_output2 = 85.67
        self.assertEqual(calculate_average_marks(students2), expected_output2)

        # Test case with 4 students
        students3 = [['CLASS', 'MARKS', 'ID', 'NAME'],
                     ['9', '95', '1', 'STUDENT1'],
                     ['8', '88', '2', 'STUDENT2'],
                     ['7', '91', '3', 'STUDENT3'],
                     ['9', '92', '4', 'STUDENT4']]
        expected_output3 = 91.50
        self.assertEqual(calculate_average_marks(students3), expected_output3)


if __name__ == "__main__":
    unittest.main()

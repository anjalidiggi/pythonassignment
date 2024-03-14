# test_case.py :-This file will contain unit tests to validate the find_day function in util.py.
import unittest
from src.Assignment7.util import find_day


class TestCalendarModule(unittest.TestCase):
    def test_find_day(self):
        # Test case with date 01 22 2024
        month1, day1, year1 = 1, 22, 2024
        expected_output1 = "MONDAY"
        self.assertEqual(find_day(month1, day1, year1), expected_output1)

        # Test case with date 12 25 2023
        month2, day2, year2 = 12, 25, 2023
        expected_output2 = "MONDAY"  # Expected output may vary depending on the date
        self.assertEqual(find_day(month2, day2, year2), expected_output2)

        # Test case with date 06 15 2025
        month3, day3, year3 = 6, 15, 2025
        expected_output3 = "SUNDAY"  # Expected output may vary depending on the date
        self.assertEqual(find_day(month3, day3, year3), expected_output3)


if __name__ == "__main__":
    unittest.main()

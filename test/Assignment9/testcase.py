# test_case.py :-This file will contain unit tests
# to validate the get_time_difference_in_seconds function in util.py.

import unittest
from src.Assignment9.util import get_time_difference_in_seconds


class TestTimeDiffereneBetweenTwoTimeStamp(unittest.TestCase):
    def test_get_time_difference_in_seconds(self):
        # Test case 1
        t1 = "Sun 10 May 2015 13:54:36 -0700"
        t2 = "Sun 10 May 2015 13:54:36 -0000"
        expected_output1 = 25200
        self.assertEqual(get_time_difference_in_seconds(t1, t2), expected_output1)

        # Test case 2
        t3 = "Sun 02 May 2015 19:54:36 +0530"
        t4 = "Sat 01 May 2015 13:54:36 -0000"
        expected_output2 = 88200
        self.assertEqual(get_time_difference_in_seconds(t3, t4), expected_output2)

        # Test case 3
        t5 = "Wed 15 Sep 2021 20:30:45 -0200"
        t6 = "Wed 15 Sep 2021 14:30:45 -0200"
        expected_output3 = 21600
        self.assertEqual(get_time_difference_in_seconds(t5, t6), expected_output3)

if __name__ == "__main__":
    unittest.main()

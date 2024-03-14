# test_case.py :-This file will contain unit tests
# to validate the get_time_difference_in_seconds function in util.py.
# test_case.py
import unittest
import numpy as np
from src.Assignment10.util import process_array


class TestFloorCeilRintForArray(unittest.TestCase):
    def test_process_array(self):
        # Test case 1
        input_str1 = "1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9"
        expected_floor1 = np.array([1., 2., 3., 4., 5., 6., 7., 8., 9.])
        expected_ceil1 = np.array([2., 3., 4., 5., 6., 7., 8., 9., 10.])
        expected_rint1 = np.array([1., 2., 3., 4., 6., 7., 8., 9., 10.])
        floor_array1, ceil_array1, rint_array1 = process_array(input_str1)
        np.testing.assert_array_equal(floor_array1, expected_floor1)
        np.testing.assert_array_equal(ceil_array1, expected_ceil1)
        np.testing.assert_array_equal(rint_array1, expected_rint1)

        # Test case 2
        input_str2 = "-1.5 0.6 4.2 3.9 5.0 -2.7"
        expected_floor2 = np.array([-2., 0., 4., 3., 5., -3.])
        expected_ceil2 = np.array([-1., 1., 5., 4., 5., -2.])
        expected_rint2 = np.array([-2., 1., 4., 4., 5., -3.])
        floor_array2, ceil_array2, rint_array2 = process_array(input_str2)
        np.testing.assert_array_equal(floor_array2, expected_floor2)
        np.testing.assert_array_equal(ceil_array2, expected_ceil2)
        np.testing.assert_array_equal(rint_array2, expected_rint2)

        # Test case 3
        input_str3 = "3.14159 2.71828 1.41421"
        expected_floor3 = np.array([3., 2., 1.])
        expected_ceil3 = np.array([4., 3., 2.])
        expected_rint3 = np.array([3., 3., 1.])
        floor_array3, ceil_array3, rint_array3 = process_array(input_str3)
        np.testing.assert_array_equal(floor_array3, expected_floor3)
        np.testing.assert_array_equal(ceil_array3, expected_ceil3)
        np.testing.assert_array_equal(rint_array3, expected_rint3)


if __name__ == "__main__":
    unittest.main()

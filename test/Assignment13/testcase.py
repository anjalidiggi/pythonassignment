# test_case.py :-This file will contain unit tests
# to validate the calculate_mean_var_std function in util.py.

import unittest
from src.Assignment13.util import calculate_mean_var_std


class TestCalculateMeanVarStd(unittest.TestCase):
    def test_calculate_mean_var_std(self):
        matrix1 = [[1, 2], [3, 4]]
        mean1, var1, std1 = calculate_mean_var_std(matrix1)
        self.assertEqual(mean1.tolist(), [1.5, 3.5])
        self.assertEqual(var1.tolist(), [1.0, 1.0])
        self.assertAlmostEqual(std1, 1.118033988749895)

        matrix2 = [[1, 1], [2, 2]]
        mean2, var2, std2 = calculate_mean_var_std(matrix2)
        self.assertEqual(mean2.tolist(), [1.0, 2.0])
        self.assertEqual(var2.tolist(), [0.25, 0.25])
        self.assertAlmostEqual(std2, 0.5)

        matrix3 = [[5, 5], [10, 10], [15, 15]]
        mean3, var3, std3 = calculate_mean_var_std(matrix3)
        self.assertEqual(mean3.tolist(), [5.0, 10.0, 15.0])
        self.assertEqual(var3.tolist(), [16.666666666666668, 16.666666666666668])
        self.assertAlmostEqual(std3, 4.08248290463863)


if __name__ == '__main__':
    unittest.main()

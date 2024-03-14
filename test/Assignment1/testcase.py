# test_case.py
import unittest
from src.Assignment1.util import calculate_average


class TestUtilFunctions(unittest.TestCase):
    def test_calculate_average(self):
        # Test case with a dictionary of scores for each student
        scores_dict = {
            "Anjali": [85, 90, 78, 92, 88],
            "DiggiByteStudent": [75, 80, 82, 90, 85],
            "Student": [70, 65, 68, 72, 75]
        }
        expected_averages = {
            "Anjali": sum(scores_dict["Anjali"]) / len(scores_dict["Anjali"]),
            "DiggiByteStudent": sum(scores_dict["DiggiByteStudent"]) / len(scores_dict["DiggiByteStudent"]),
            "Student": sum(scores_dict["Student"]) / len(scores_dict["Student"])
        }
        self.assertDictEqual(calculate_average(scores_dict), expected_averages)

    def test_empty_scores(self):
        # Test case with an empty dictionary of scores
        scores_dict = {}
        self.assertDictEqual(calculate_average(scores_dict), {})

    def test_single_student(self):
        # Test case with a single student
        scores_dict = {"Anjali": [85, 90, 78, 92, 88]}
        expected_averages = {"Anjali": sum(scores_dict["Anjali"]) / len(scores_dict["Anjali"])}
        self.assertDictEqual(calculate_average(scores_dict), expected_averages)

    def test_multiple_students_same_scores(self):
        # Test case with multiple students having the same scores
        scores_dict = {
            "Anjali": [75, 75, 75, 75, 75],
            "Student1": [75, 75, 75, 75, 75],
            "Student2": [75, 75, 75, 75, 75]
        }
        expected_average = sum(scores_dict["Anjali"]) / len(scores_dict["Anjali"])
        expected_averages = {"Anjali": expected_average, "Student1": expected_average, "Student2": expected_average}
        self.assertDictEqual(calculate_average(scores_dict), expected_averages)


if __name__ == "__main__":
    unittest.main()

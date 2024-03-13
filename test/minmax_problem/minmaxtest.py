import unittest
from src.minmax_problem.util import min_max_axis_1


class MyTestCase(unittest.TestCase):
    def test_case(self):
        matrix = [[4, 2], [2, 5], [3, 7], [1, 3], [4, 0]]
        actual_output = min_max_axis_1(matrix)
        expected_output = 3
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case1(self):
        matrix = [[4, 3], [8, 7], [2, 7], [6, 2], [4, 1]]
        actual_output = min_max_axis_1(matrix)
        expected_output = 7
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

import unittest
from src.linearalgebra_problem.util import calculate_determinant


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = calculate_determinant([[1.1, 1.1], [1.1, 1.1]])
        expected_output = 0.0
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case2(self):
        actual_output = calculate_determinant([[1, 2], [2, 1]])
        expected_output = -3.0
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

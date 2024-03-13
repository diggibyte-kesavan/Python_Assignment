import unittest
from src.linearalgebra_problem.util import calculate_determinant


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_output = calculate_determinant([[1.1, 1.1], [1.1, 1.1]])
        expected_output = 0.0
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()

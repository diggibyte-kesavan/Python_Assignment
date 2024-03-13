import unittest
from src.noidea_problem.util import calculate_happiness_noidea


class MyTestCase(unittest.TestCase):
    def test_something(self):
        n, m = 3, 2
        arr = [3, 1, 5]
        A = [3, 1]
        B = [5, 7]
        actual_output = calculate_happiness_noidea(n, m, arr, A, B)
        expected_output = 1
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()

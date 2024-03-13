import unittest
from src.noidea_problem.util import calculate_happiness_noidea


class MyTestCase(unittest.TestCase):
    def test_case(self):
        n, m = 3, 2
        arr = [3, 1, 5]
        A = [3, 1]
        B = [5, 7]
        actual_output = calculate_happiness_noidea(n, m, arr, A, B)  # total happiness = 1 + 1 - 1 = 1.
        expected_output = 1
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case2(self):
        n, m = 4, 3
        arr = [1, 2, 3, 4]
        A = [1, 3]
        B = [2]
        actual_output = calculate_happiness_noidea(n, m, arr, A, B)  # total happiness = 1 - 1 + 1 + 0 = 1.
        expected_output = 1
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

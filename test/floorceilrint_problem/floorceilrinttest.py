import unittest
from src.floorceilrint_problem.util import floor_ceil_rint


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = floor_ceil_rint([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9])
        expected_output = "[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]\n[  2.   3.   4.   5.   6.   7.   8.   9.  10.]\n[  1.   2.   3.   4.   6.   7.   8.   9.  10.]"
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        actual_output = floor_ceil_rint([1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9, 2.2, 3.2])
        expected_output = "[ 1.  2.  3.  4.  5.  6.  7.  8.  9.  2.  3.]\n[  2.   3.   4.   5.   6.   7.   8.   9.  10.   3.   4.]\n[  1.   2.   3.   4.   6.   7.   8.   9.  10.   2.   3.]"
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

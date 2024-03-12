import unittest
from src.stringformat_problem.util import print_formatted


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = print_formatted(2)
        expected_output = "1  1  1  1\n2  2  2 10"
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case1(self):
        actual_output = print_formatted(3)
        expected_output = "1  1  1  1\n2  2  2 10\n3  3  3 11"
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

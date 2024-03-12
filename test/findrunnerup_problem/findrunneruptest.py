import unittest
from src.findrunnerup_problem.util import runner_up_score


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = runner_up_score([67, 68, 69])
        expected_output = 68
        self.assertEqual(actual_input, expected_output)

    def test_case2(self):
        actual_input = runner_up_score([25, 26.5, 28])
        expected_output = 26.5
        self.assertEqual(actual_input, expected_output)

    def test_case3(self):
        actual_input = runner_up_score([2, 3, 5, 6, 7, 7,7])
        expected_output = 6
        self.assertEqual(actual_input, expected_output)


if __name__ == '__main__':
    unittest.main()

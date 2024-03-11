import unittest
from src.percentage_problem.util import *


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = percent_calc({'Krishna': [67, 68, 69], 'Arjun': [70, 98, 63], 'Malika': [52, 56, 60]}, 'Malika')
        expected_output = 56
        self.assertEqual(actual_input, format(expected_output, '.2f'))
        # self.assertEqual(True, False)  # add assertion here

    def test_case2(self):
        actual_input = percent_calc({'Harsh': [25, 26.5, 28], 'Anurag': [26, 28, 30]}, 'Harsh')
        expected_output = 26.5
        self.assertEqual(actual_input, format(expected_output, '.2f'))


if __name__ == '__main__':
    unittest.main()



import unittest
from src.percentage_problem.util import *


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = percent_calculation({'Kesavan': [67, 68, 69], 'Aravind': [70, 98, 63], 'Bala': [52, 56, 60]}, 'Kesavan')
        expected_output = 68
        self.assertEqual(actual_input, format(expected_output, '.2f'))
        # self.assertEqual(True, False)  # add assertion here

    def test_case2(self):
        actual_input = percent_calculation({'Priya': [25, 26.5, 28], 'Kishore': [26, 28, 30]}, 'Priya')
        expected_output = 26.5
        self.assertEqual(actual_input, format(expected_output, '.2f'))


if __name__ == '__main__':
    unittest.main()



import unittest
from src.calendermodule_problem.util import find_day_of_date


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = find_day_of_date("08 05 2020")
        expected_output = "WEDNESDAY"
        self.assertEqual(actual_output, expected_output)  # add assertion here




if __name__ == '__main__':
    unittest.main()

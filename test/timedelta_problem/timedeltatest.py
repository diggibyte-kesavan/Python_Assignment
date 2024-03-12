import unittest
from src.timedelta_problem.util import time_difference


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = time_difference("Sun 10 May 2015 13:54:36 -0700", "Sun 10 May 2015 13:54:36 -0000")
        expected_output = 25200
        self.assertEqual(actual_output, expected_output)  # add assertion here

    def test_case1(self):
        actual_output = time_difference("Sat 02 May 2015 19:54:36 +0530", "Fri 01 May 2015 13:54:36 -0000")
        expected_output = 88200
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

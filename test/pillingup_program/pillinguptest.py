import unittest
from src.pillingup_program.util import piling_up


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_output = piling_up(1,[[4, 3, 2, 1, 3, 4]])
        expected_output = "Yes"
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()

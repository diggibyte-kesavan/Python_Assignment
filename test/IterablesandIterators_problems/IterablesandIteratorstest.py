import unittest
from src.IterablesandIterators_program.util import iterables_iterators


class MyTestCase(unittest.TestCase):
    def test_something(self):
        actual_output = iterables_iterators(4, "aacd", 2)
        expected_output = 0.8333333
        self.assertEqual(actual_output, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()

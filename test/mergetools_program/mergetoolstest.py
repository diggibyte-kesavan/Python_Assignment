import unittest
from src.mergetools_program.util import merge_the_tools


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_output = merge_the_tools("AABCAAADA", 3)
        expected_output = 'AB\nCA\nAD'
        self.assertEqual(actual_output, expected_output)

    def test_case1(self):
        actual_output = merge_the_tools("kkalmmkjh", 3)
        expected_output = "ka\nlm\nkjh"
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

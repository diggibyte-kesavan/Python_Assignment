import unittest
from src.wordorder_problem.util import word_order


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = word_order(4, ['bcdef', 'abcdefg', 'bcde', 'bcdef'])
        expected_output = (3, [2, 1, 1])
        self.assertEqual(actual_input, expected_output)  # add assertion here




if __name__ == '__main__':
    unittest.main()

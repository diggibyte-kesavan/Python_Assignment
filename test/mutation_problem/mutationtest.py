import unittest
from src.mutation_problem.util import mutate_string


class MyTestCase(unittest.TestCase):
    def test_case(self):
        actual_input = mutate_string("aron", 0, "m")
        expected_output = "mron"
        self.assertEqual(actual_input, expected_output)  # add assertion here

    def test_case1(self):
        actual_input = mutate_string("mam", 2, "n")
        expected_output = "man"
        self.assertEqual(actual_input, expected_output)  # add assertion here


if __name__ == '__main__':
    unittest.main()

import unittest
from src.namedtuple_problem.util import calculate_average_mark


class TestCalculateAverageMark(unittest.TestCase):
    def test_case(self):
        students_data = [
            "5",
            "ID MARKS NAME CLASS",
            "1 97 aaron 7",
            "2 50 david 4",
            "3 91 anbu 9",
            "4 72 edward 5",
            "5 80 alex 6"
        ]

        actual_output = calculate_average_mark(students_data)
        expected_output = '78.00'
        self.assertEqual(actual_output, expected_output)

    def test_case2(self):
        students_data = [
            "5",
            "ID MARKS NAME CLASS",
            "1 91 kesavan 7",
            "2 75 suresh 4",
            "3 76 arun 9",
            "4 98 akila 5",
            "5 89 priya 6"
        ]

        actual_output = calculate_average_mark(students_data)
        expected_output = '85.80'
        self.assertEqual(actual_output, expected_output)


if __name__ == '__main__':
    unittest.main()

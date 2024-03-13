import unittest
from src.validateemail_problem.util import validate_email


class MyTestCase(unittest.TestCase):
    def test_case(self):
        valid_email = "kesavan@example.com"
        self.assertTrue(validate_email(valid_email))

    def test_case1(self):
        valid_email = "kumar@gmail.com"
        self.assertTrue(validate_email(valid_email))

if __name__ == '__main__':
    unittest.main()

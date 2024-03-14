# test_case.py :-This file will contain unit tests
# to validate the extract_valid_emails function in util.py
#  It validates email addresses and returns a list containing
#  only the valid ones in lexicographical order.
#  The unit tests validate the correctness of the solution.
import unittest
from src.Assignment18.util import extract_valid_emails


class TestExtractValidEmails(unittest.TestCase):
    def test_extract_valid_emails(self):
        self.assertEqual(
            extract_valid_emails(3, ['anjali@diggibyte.com', 'gaytri@diggibyte.com', 'laxmi@diggibyte.com']),
            ['anjali@diggibyte.com', 'gaytri@diggibyte.com', 'laxmi@diggibyte.com'])
        self.assertEqual(
            extract_valid_emails(4, ['anjali@diggibyte.com', 'test', 'test@diggibyte', 'laxmi@diggibyte.com']),
            ['anjali@diggibyte.com', 'laxmi@diggibyte.com'])


if __name__ == '__main__':
    unittest.main()

import unittest, sys

sys.path.append('../SustainabiliMe') # imports python file from parent directory
from . import app


def test_invalid_username_registration(self):
    response = self.register('t', 'test@example.com', 'FlaskIsAwesome')
    self.assertIn(b'Field must be between 2 and 20 characters long.', response.data)

def test_invalid_email_registration(self):
    response = self.register('test2', 'test@example', 'FlaskIsAwesome')
    self.assertIn(b'Invalid email address.', response.data)


if __name__ == "__main__":
    unittest.main()
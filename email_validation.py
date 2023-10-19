

import re

def is_valid_email(email):
    # Define a regular expression pattern for email validation
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    
    # Use the re.match function to check if the email matches the pattern
    return re.match(email_pattern, email) is not None


import unittest

# Import the is_valid_email function from your email validation module
from email_validation import is_valid_email

class TestEmailValidation(unittest.TestCase):
    def test_valid_email(self):
        # Test with a valid email address
        valid_email = "user@example.com"  # Change this to a valid email address
        self.assertTrue(is_valid_email(valid_email))

    def test_invalid_email(self):
        # Test with an invalid email address
        invalid_email = "invalid-email"  # Change this to an invalid email address
        self.assertFalse(is_valid_email(invalid_email))

if __name__ == "__main__":
    unittest.main()
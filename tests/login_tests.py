from __init__ import *

# Sample user data to test
sampleUser1 = {
    "name": "Noelle",
    "email": "noelle123@example.com",
    "password": "holidays"
}
# I don't think we've decided on user ID assignment yet.

class LoginTestSuite(unittest.TestCase):
    user = None

    def test_duplicate_emails(self):
        pass # TODO

    def test_login_success_after_account_creation(self):
        pass

    def test_successful_logout(self):
        pass

    
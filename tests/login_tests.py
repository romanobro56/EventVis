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
    mockoDB_client = Mock(spec=MongoClient)
    mockoDB_client

    def setup(self):
        client = mongomock.MongoClient()
        database = client.__getattr__('event_vis')
        allUsers = database['users']
        allEvents = database['events']
        print(allUsers, allEvents)
    

    def test_duplicate_emails(self):
        # Assume we get the user-submitted input data from the front-end.
        self.fail("Testing...")
        pass # TODO

    def test_login_success_after_account_creation(self):
        pass

    def test_successful_logout(self):
        pass

    def test_failed_login_after_wrong_password(self):
        pass

def main():
    lts = LoginTestSuite()
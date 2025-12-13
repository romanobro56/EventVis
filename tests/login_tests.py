import sys

from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
sys.path.append("./tests")
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
    client = None 
    database = None
    allUsers = None
    allEvents = None


    # TODO: Figure out how to make this portable to other testing files.
    def setup(self):
        self.client = mongomock.MongoClient()
        self.database = self.client.__getattr__('event_vis')
        self.allUsers = self.database['users']
        self.allEvents = self.database['events']
    

    def test_duplicate_emails(self):
        # Assume we get the user-submitted input data from the front-end.
        self.setup()
        user_json = json.dumps(sampleUser1)
        print(user_json)
        create_user(user_json)
        create_user(str(sampleUser1))
        # create_user(str(JSONResponse(content=jsonable_encoder(obj=sampleUser1))))
        self.assertEqual(1, self.allUsers.count_documents(), "Only 1 user was created.")
        
        pass # TODO

    def test_login_success_after_account_creation(self):
        pass

    def test_successful_logout(self):
        pass

    def test_failed_login_after_wrong_password(self):
        pass

def main():
    lts = LoginTestSuite()
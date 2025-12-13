from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from typing import Collection
import unittest 
import sys, os
from backend.app import User
from unittest.mock import Mock, patch
import mongomock
import json
sys.path.append("../backend/db")
sys.path.append("./backend/apps/routers")
sys.path.append("./backend/db")
# from backend.db.database_client import *
import backend.db.database_client as bddc
from backend.app.models.user_models import SignupRequest, LoginRequest
from backend.app.routers.users import signup

# Sample user data to test
sampleUser1 = {
    "name": "Noelle",
    "email": "noelle123@example.com",
    "password": "holidays"
}

sampleUser2 = SignupRequest(name="Noelle", password="holidays", email="noelle123@example.com")

class LoginTestSuite(unittest.TestCase):
    user = None
    mockoDB_client = Mock(spec=bddc.MongoClient)
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
    
    @patch("backend.app.routers.users.signup")
    def test_duplicate_emails(self, signup_mock):
        # Assume we get the user-submitted input data from the front-end.
        self.setup()

        signup_mock.side_effect = 3
        
        user_json = json.dumps(sampleUser1)
        backend.app.routers.users.signup(sampleUser2)
        print(backend.app.routers.users.signup(sampleUser2))
        self.assertEqual(1, self.allUsers.count_documents({}), "Only 1 user was supposed to be created.")
        
        pass # TODO

    def test_login_success_after_account_creation(self):
        pass

    def test_successful_logout(self):
        pass

    def test_failed_login_after_wrong_password(self):
        pass

def main():
    lts = LoginTestSuite()
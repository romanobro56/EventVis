
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

import os

username = os.environ.get('USRNM')
password = os.environ.get('PASS')

print(username)
print(password)

uri = f"mongodb+srv://{username}:{password}@eventviscluster.dpmc4qx.mongodb.net/?appName=EventVisCluster"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
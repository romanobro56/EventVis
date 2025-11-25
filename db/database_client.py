
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

import os

#set your MongoDB username and password to these environment variables
username = os.environ.get('USRNM')
password = os.environ.get('PASS')



#generate the connection string
uri = f"mongodb+srv://{username}:{password}@eventviscluster.dpmc4qx.mongodb.net/?appName=EventVisCluster"

def connect_cluster():
    # Create a new client and connect to the server
    try:
        client = MongoClient(uri, server_api=ServerApi('1'))
    except ConnectionFailure as e:
        return e
    return client
    
def close_connection(client):
    
    return

def create_user(user: str):
    #TODO
    return

def update_events_campus_pulse():
    return

def update_events_calendar():
    return

def create_new_event(event: str):
    #TODO
    return
   

def delete_event(event: str):
    #TODO
    return
  

def get_events(query: str):
    #TODO
    return
   

def delete_user(user: str):
    #TODO
    return


# Send a ping to confirm a successful connection


#for testing
print(username)
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    database = client.get_database("sample_mflix")
    movies = database.get_collection("movies")
    # Query for a movie that has the title 'Back to the Future'
    query = { "title": "Back to the Future" }
    movie = movies.find_one(query)
    print(movie)
    client.close()
except Exception as e:
    print(e)

        

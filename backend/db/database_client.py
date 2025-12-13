import json
import os

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ConnectionFailure

from dotenv import load_dotenv

from .scraping.campus_pulse_scraping import scrape_campus_pulse
from .scraping.events_calendar_scraping import scrape_umass_events

load_dotenv()

username = os.getenv('USRNM')
password = os.getenv('PASS')

# print(username)
# print(password)

#generate the connection string
uri = f"mongodb+srv://{username}:{password}@eventviscluster.dpmc4qx.mongodb.net/?appName=EventVisCluster"
client = MongoClient(uri, server_api=ServerApi('1'))

#get the EventVis database from the cluster
db = client['event_vis']

#get the collections for each object type
user_collection = db['users']
comment_collection = db['comments']
event_collection = db['events']

#need to add validation to these, but they work for now!
def create_user(user: str):
    user_dict = json.loads(str)
    user_collection.insert_one(user_dict)
    return

def update_events_campus_pulse():
    events = scrape_campus_pulse()
    for event in events:
        event_dict = json.loads(event)
        event_collection.insert_one(event_dict)
    return

def update_events_calendar():
    events = scrape_umass_events()
    for event in events:
        event_dict = json.loads(event)
        event_collection.insert_one(event_dict)
    return

def create_new_event(event: str):
    event_dict = json.loads(str)
    event_collection.insert_one(event_dict)
    return
   

def delete_event(event: str):
    event_dict = json.loads(event)
    event_collection.delete_one(event_dict)
    return
  

#returns a list of JSON strings of each event that matches the query
#assumes a JSON input, e.g. '{"name": "Bob"}'
def get_events(query: str):
    query_dict = json.loads(query)
    event_documents = event_collection.find(query_dict)
    output_json = []
    for document in event_documents:
        output_document = json.dumps(document)
        output_json.append(output_document)
    return output_json

#Returns a list of JSON strings of every event in the database
def get_all_events():
    event_documents = event_collection.find()
    output_json = []
    for document in event_documents:
        output_document = json.dumps(document)
        output_json.append(output_document)
    return output_json

#deletes a user given a JSON string matching the user's document
def delete_user(user: str):
    user_dict = json.loads(user)
    event_collection.delete_one(user_dict)
    return


# Send a ping to confirm a successful connection

if __name__ == "__main__":
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

    client.close()

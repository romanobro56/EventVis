import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class MongoDB:
    def __init__(self):
        self.client = None
        self.database = None
    
    def connect(self):
        """Connect to MongoDB using environment variables"""
        try:
            username = os.getenv('USRNM')
            password = os.getenv('PASS')
            cluster = "eventviscluster.dpmc4qx.mongodb.net"  # Your cluster from the URI
            database_name = os.getenv('DATABASE_NAME', 'eventvis')
            
            if not username or not password:
                raise ValueError("MongoDB username or password not set in environment variables")
            
            uri = f"mongodb+srv://{username}:{password}@{cluster}/?retryWrites=true&w=majority&appName=EventVisCluster"
            
            # Create a new client and connect to the server
            self.client = MongoClient(uri, server_api=ServerApi('1'))
            self.database = self.client[database_name]
            
            # Send a ping to confirm successful connection
            self.client.admin.command('ping')
            print("Successfully connected to MongoDB!")
            
        except Exception as e:
            print(f"MongoDB connection failed: {e}")
            raise
    
    def close(self):
        """Close MongoDB connection"""
        if self.client:
            self.client.close()
            print("MongoDB connection closed")

# Global database instance
mongodb = MongoDB()

def get_database():
    """Get database instance"""
    if not mongodb.database:
        mongodb.connect()
    return mongodb.database

def get_event_collection():
    """Get events collection"""
    return get_database().events

def get_user_collection():
    """Get users collection"""
    return get_database().users

def get_comment_collection():
    """Get comments collection"""
    return get_database().comments

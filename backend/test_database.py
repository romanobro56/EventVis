import os
import sys
from dotenv import load_dotenv

# Add current directory to path
sys.path.append(os.path.dirname(__file__))

from app.database import mongodb

def test_connection():
    print("Testing MongoDB Connection...")
    
    try:
        # Check environment variables first
        from check_env import check_environment
        if not check_environment():
            return
        
        # Test database connection
        mongodb.connect()
        
        # Test database operations
        db = mongodb.database
        print(f"Connected to database: {db.name}")
        
        # List collections
        collections = db.list_collection_names()
        print(f"Collections: {collections}")
        
        # Test events collection
        events = db.events
        print(f"Events collection accessible: {events.name}")
        
        print("All tests passed! MongoDB is properly configured.")
        
    except Exception as e:
        print(f"Test failed: {e}")
    finally:
        mongodb.close()

if __name__ == "__main__":
    test_connection()
from fastapi import FastAPI, Request, HTTPException, Depends, Query, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from clerk_backend_api import Clerk, Session
import os
from starlette.responses import FileResponse
from pathlib import Path
import hashlib
from __init__ import *
import random
from pydantic import BaseModel
from ...db.database_client import * # This may require changing a Python path.

app = FastAPI()

from dotenv import load_dotenv

origins = [
    "http://localhost:5173",
    "localhost:5173",
]

load_dotenv()

# I don't know if I'm getting a Clerk API Key correctly.
clerk = Clerk(bearer_auth=os.getenv("CLERK_SECRET_KEY"))

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Create an account using data from the arguments. The parameters may need to be changed.
def create_account(password: str, name: str, email: str) -> User:
    hashValue = hashlib.sha3_256(password.encode())

    # This is a temporary way to make a user ID that is unlikely to lead to collisions.
    user_id: int = random.randbytes(1) ** random.randbytes(1)

    user_object = User(user_id, name, email, hashValue)
    user_json = JSONResponse(content=jsonable_encoder(user_object))

    # Send the data to MongoDB via the API calls.
    create_user(str(user_json)) # could be email or name

    # Return (if needed)
    return user_object

    # TODO: Consider duplicate emails.

# Attempt to log in with the user's data. This likely needs to change, too.
def attempt_login(email: str, password: str):
    # It's unlikely for an incorrect password to get accepted because it shared the correct SHA-3 hash.
    hashValue = hashlib.sha3_256(password.encode())

    # I think we need to send the email and hashValue variables to MongoDB to check for a database?

# I'm assuming this is akin to the "access denied" page for non-logged-in users.
@app.get("/protected")
async def protected(req: Request):
    # Get the session token...
    authorizationHeader = req.headers.get("Authorization")
    if not authorizationHeader or not authorizationHeader.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="The Authorization Header is missing or invalid.")
    
    sessionToken = authorizationHeader.split(" ")[1]

    # Use Clerk's API to verify this token...
    try:
        session: Session = Clerk.authenticate_request(clerk, req)
        if not session:
            raise HTTPException(status_code=401, detail="The Session is invalid.")
    except Exception as exc:
        raise HTTPException(status_code=401, detail=str(exc))

@app.get("/public")
async def public():
    return {"message": "Welcome to EventVis! Don't forget to sign in or sign up!"}

@app.get("/")
async def index():
    # This assumes you're running the server from the "EventVis" root folder.
    finalPath = Path.cwd() / "frontend" / "index.html"

    return FileResponse(finalPath)

# What we need: Login system that puts username & password to MongoDB
# this schema is used by the front-end
class Event(BaseModel):
    id: int
    title: str
    date: str
    description: str
    full_description: str
    start_time: str
    end_time: str
    location: str
    lat: float
    lng: float

# latitudes and longitudes are probably wrong
DUMMY_EVENTS = [
  Event(
    id=1,
    title="Farmers Market",
    date="Nov 10",
    description="Local produce and crafts",
    full_description="Come enjoy fresh local produce, crafts, and music at the farmers market!",
    start_time="09:00",
    end_time="15:00",
    location="Central Park",
    lat=42.3736,
    lng=-72.5199,
  ),
  Event(
    id=2,
    title="Art in the Park",
    date="Nov 12",
    description="Outdoor art showcase",
    full_description="Experience local artists showcasing their work in a beautiful outdoor setting.",
    start_time="11:00",
    end_time="17:00",
    location="Riverside Park",
    lat=42.376,
    lng=-72.52,
  ),
  Event(
    id=3,
    title="Food Festival",
    date="Nov 15",
    description="Tasty eats and live music",
    full_description="Sample cuisines from around the world while enjoying live performances.",
    start_time="12:00",
    end_time="20:00",
    location="Downtown Square",
    lat=42.375,
    lng=-72.520
  ),
]

DUMMY_EVENT = DUMMY_EVENTS[0]

"""
Create event
"""
@app.post("/events")
def create_event(event: Event):
    # MongoDB API call to make a new event in the database
    create_new_event(str(JSONResponse(content=jsonable_encoder(event))))

    # returns id of created event (We have not set up event ID disambiguation yet.)
    return 0

"""
Edit event
"""
@app.put("/events/{event_id}")
def edit_event(event_id: int, new_event: Event):
    return

"""
Cancel event
"""
@app.put("/events/{event_id}/cancel")
def cancel_event(event_id: int):
    return

"""
Get event details
"""
@app.get("/events/{event_id}")
def get_event(event_id: int):
    return DUMMY_EVENT

"""
RSVP for event
"""
@app.put("/events/{event_id}/rsvp")
def rsvp_for_event(event_id: int):
    return

"""
Un-RSVP for event
"""
@app.put("/events/{event_id}/unrsvp")
def unrsvp_for_event(event_id: int):
    return

"""
Comment on event
"""
@app.post("/events/{event_id}/comments")
def comment_on_event(event_id: int, comment_text: str):
    # returns id of new comment
    return 0

"""
Search for events
Arguments: search_text, tags, user_location, radius, time
"""
@app.get("/events")
# can add other search parameters like tags, location, etc
def search_for_events(search_text: str):
    return DUMMY_EVENTS

@app.get("/settings/")
def get_user_preferences(user_id: int):
    return {"user_id": user_id}

from fastapi import FastAPI, Request, HTTPException, Depends, Query
from fastapi.middleware.cors import CORSMiddleware
from clerk_backend_api import Clerk, Session
from fastapi.middleware.cors import CORSMiddleware
import os
from starlette.responses import FileResponse
from pathlib import Path
import hashlib
from __init__ import *
import random

app = FastAPI()

from dotenv import load_dotenv

origins = [
    "http://localhost:5173",
    "localhost:5173"
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

    # Still need to figure out how to send this to MongoDB later...
    return User(user_id, name, email, hashValue)

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

"""
Each of these is a routing method;
There's one for the list view and the map view,
and I added one for specific events and user profile views.

Returns and types are just there for convenience and don't mean anything.
You can change those once this is actually implemented.
"""
@app.get("/map/")
def read_root():
    return {"Hello": "World"}

@app.get("/list/")
def read_item():
    return {"list": "list"}

@app.get("/event/{event_id}")
def get_event(event_id):
    return {"event": event_id}

@app.get("/user/{user_id}")
def get_user(user_id):
    return {"user": user_id}

"""
These are utilities, like setting and posting for actually creating an event.
This could probably be its own file, too.
"""

@app.post("/event/{event_id}")
def create_event(event_id):
    return {"event_created": event_id}

@app.get("/settings/")
def get_user_preferences(user_id):
    return {"user_id": user_id}
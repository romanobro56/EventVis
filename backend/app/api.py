# app/api.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users, events, public

app = FastAPI()

origins = ["http://localhost:5173", "localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(users.router)
app.include_router(events.router)
app.include_router(public.router)

if __name__ == "__main__":
    for route in app.routes:
        print(f"Path: {route.path} | Methods: {route.methods} | Name: {route.name}")




"""from fastapi import FastAPI, Request, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from pathlib import Path
from pydantic import BaseModel
from datetime import datetime
import hashlib
import secrets
from bson.objectid import ObjectId

# Import your MongoDB client
from db.database_client import client



# --- MongoDB setup ---
db = client["event_vis"]
users_col = db["users"]

# --- FastAPI setup ---
app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# --- Helper functions ---
def hash_password(password: str) -> str:
    return hashlib.sha3_256(password.encode()).hexdigest()

def create_session_token() -> str:
    return secrets.token_hex(32)

def find_user_by_email(email: str):
    return users_col.find_one({"email": email})

def find_user_by_token(token: str):
    return users_col.find_one({"session_token": token})

# --- User models ---
class SignupRequest(BaseModel):
    name: str
    email: str
    password: str

class LoginRequest(BaseModel):
    email: str
    password: str

# --- User endpoints ---
@app.post("/signup")
async def signup(data: SignupRequest):
    if find_user_by_email(data.email):
        raise HTTPException(status_code=409, detail="Email already in use.")

    user_doc = {
        "name": data.name,
        "email": data.email,
        "password_hash": hash_password(data.password),
        "session_token": None,
        "created_at": datetime.utcnow(),
    }

    result = users_col.insert_one(user_doc)
    return {"success": True, "user_id": str(result.inserted_id)}

@app.post("/login")
async def login(data: LoginRequest):
    user = find_user_by_email(data.email)
    if not user or user["password_hash"] != hash_password(data.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_session_token()
    users_col.update_one({"_id": user["_id"]}, {"$set": {"session_token": token, "last_login": datetime.utcnow()}})

    return {"access_token": token, "token_type": "bearer", "user_id": str(user["_id"]), "name": user["name"]}

@app.get("/protected")
async def protected(req: Request):
    authorizationHeader = req.headers.get("Authorization")
    if not authorizationHeader or not authorizationHeader.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid.")
    
    token = authorizationHeader.split(" ")[1]
    user = find_user_by_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Session is invalid or expired.")

    return {
        "user_id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"]
    }

@app.post("/logout")
async def logout(req: Request):
    authorizationHeader = req.headers.get("Authorization")
    if not authorizationHeader or not authorizationHeader.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid.")

    token = authorizationHeader.split(" ")[1]
    user = find_user_by_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token.")

    users_col.update_one({"_id": user["_id"]}, {"$set": {"session_token": None}})
    return {"success": True, "message": "Logged out"}

# --- Event models ---
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

# Dummy events
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

# --- Event endpoints ---
@app.post("/events")
def create_event(event: Event):
    return 0

@app.put("/events/{event_id}")
def edit_event(event_id: int, new_event: Event):
    return

@app.put("/events/{event_id}/cancel")
def cancel_event(event_id: int):
    return

@app.get("/events/{event_id}")
def get_event(event_id: int):
    return DUMMY_EVENT

@app.put("/events/{event_id}/rsvp")
def rsvp_for_event(event_id: int):
    return

@app.put("/events/{event_id}/unrsvp")
def unrsvp_for_event(event_id: int):
    return

@app.post("/events/{event_id}/comments")
def comment_on_event(event_id: int, comment_text: str):
    return 0

@app.get("/events")
def search_for_events(search_text: str):
    return DUMMY_EVENTS

@app.get("/settings/")
def get_user_preferences(user_id: int):
    return {"user_id": user_id}

# --- Public endpoint ---
@app.get("/public")
async def public():
    return {"message": "Welcome to EventVis! Don't forget to sign in or sign up!"}

@app.get("/")
async def index():
    finalPath = Path.cwd() / "frontend" / "index.html"
    return FileResponse(finalPath)
"""
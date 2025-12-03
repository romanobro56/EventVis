from fastapi import APIRouter, HTTPException, Request
from db.database_client import client
from app.models.user_models import SignupRequest, LoginRequest
from datetime import datetime
import hashlib, secrets
from bson import ObjectId

router = APIRouter(prefix="/users", tags=["users"])

db = client["event_vis"]
users_col = db["users"]
events_col = db["events"]

# ------------------ HELPERS ------------------
def hash_password(password: str) -> str:
    return hashlib.sha3_256(password.encode()).hexdigest()

def create_session_token() -> str:
    return secrets.token_hex(32)

def find_user_by_email(email: str):
    return users_col.find_one({"email": email})

def find_user_by_token(token: str):
    return users_col.find_one({"session_token": token})


# ------------------ SIGNUP ------------------
@router.post("/signup")
async def signup(data: SignupRequest):
    if find_user_by_email(data.email):
        raise HTTPException(status_code=409, detail="Email already in use.")

    token = create_session_token()

    user_doc = {
        "name": data.name,
        "email": data.email,
        "password_hash": hash_password(data.password),
        "session_token": token,
        "created_at": datetime.utcnow(),
        "saved_events": []
    }

    result = users_col.insert_one(user_doc)

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": str(result.inserted_id),
        "name": data.name
    }


# ------------------ LOGIN ------------------
@router.post("/login")
async def login(data: LoginRequest):
    user = find_user_by_email(data.email)
    if not user or user["password_hash"] != hash_password(data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_session_token()

    users_col.update_one(
        {"_id": user["_id"]},
        {"$set": {"session_token": token, "last_login": datetime.utcnow()}}
    )

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": str(user["_id"]),
        "name": user["name"]
    }


# ------------------ PROTECTED ROUTE ------------------
@router.get("/protected")
async def protected(req: Request):
    token_header = req.headers.get("Authorization")

    if not token_header or not token_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing auth")

    token = token_header.split(" ")[1]
    if token in ["null", "undefined", "", None, "None"]:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = find_user_by_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid session")

    return {
        "user_id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
    }


# ------------------ GET SAVED EVENTS ------------------
@router.get("/saved")
async def get_saved_events(req: Request):
    token_header = req.headers.get("Authorization")
    if not token_header or not token_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = token_header.split(" ")[1]

    if token in ["null", "undefined", "", None, "None"]:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = users_col.find_one({"session_token": token})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid session")

    saved_ids = user.get("saved_events", [])

    valid_ids = [sid for sid in saved_ids if ObjectId.is_valid(sid)]
    event_objects = list(events_col.find({"_id": {"$in": [ObjectId(i) for i in valid_ids]}}))

    for e in event_objects:
        e["_id"] = str(e["_id"])

    return {"saved_events": event_objects}

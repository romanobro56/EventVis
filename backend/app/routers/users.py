# app/routers/users.py
from fastapi import APIRouter, HTTPException, Request
from db.database_client import client
from app.models.user_models import SignupRequest, LoginRequest
from datetime import datetime
import hashlib, secrets

router = APIRouter(prefix="/users", tags=["users"])

# MongoDB
db = client["event_vis"]
users_col = db["users"]

# Helper functions
def hash_password(password: str) -> str:
    return hashlib.sha3_256(password.encode()).hexdigest()

def create_session_token() -> str:
    return secrets.token_hex(32)

def find_user_by_email(email: str):
    return users_col.find_one({"email": email})

def find_user_by_token(token: str):
    return users_col.find_one({"session_token": token})

# Endpoints
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
    }
    result = users_col.insert_one(user_doc)

    return {
        "access_token": token,
        "token_type": "bearer",
        "user_id": str(result.inserted_id),
        "name": data.name
    }


@router.post("/login")
async def login(data: LoginRequest):
    user = find_user_by_email(data.email)
    if not user or user["password_hash"] != hash_password(data.password):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    token = create_session_token()
    users_col.update_one(
        {"_id": user["_id"]},
        {"$set": {"session_token": token, "last_login": datetime.utcnow()}}
    )
    print(f"[DEBUG] User {user['_id']} logged in with token {token}")
    return {"access_token": token, "token_type": "bearer", "user_id": str(user["_id"]), "name": user["name"]}

@router.post("/logout")
async def logout(req: Request):
    authorization = req.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Authorization header missing or invalid.")

    token = authorization.split(" ")[1]
    user = find_user_by_token(token)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token.")

    users_col.update_one({"_id": user["_id"]}, {"$set": {"session_token": None}})
    print(f"[DEBUG] User {user['_id']} logged out")
    return {"success": True, "message": "Logged out"}

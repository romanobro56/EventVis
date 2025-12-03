# app/routers/events.py
from fastapi import APIRouter, HTTPException, Request
from bson import ObjectId
from db.database_client import client
from app.models.event_models import EventModel

router = APIRouter(prefix="/events", tags=["events"])

db = client["event_vis"]
events_col = db["events"]
users_col = db["users"]

# Convert MongoDB event → JSON
def serialize_event(event):
    event["_id"] = str(event["_id"])
    return event


# ----------------------- GET ALL EVENTS -----------------------
@router.get("/")
async def get_events():
    events = list(events_col.find())
    return [serialize_event(e) for e in events]


# ----------------------- GET ONE EVENT -----------------------
@router.get("/{event_id}")
async def get_event(event_id: str):
    if not ObjectId.is_valid(event_id):
        raise HTTPException(status_code=400, detail="Invalid event ID")

    event = events_col.find_one({"_id": ObjectId(event_id)})
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")

    return serialize_event(event)


# ----------------------- CREATE EVENT -----------------------
@router.post("/")
async def create_event(event: EventModel):
    event_doc = event.dict()
    result = events_col.insert_one(event_doc)
    return {"event_id": str(result.inserted_id), "message": "Event created"}


# ------------------ TOKEN VALIDATION HELPER ------------------
def validate_token(req: Request):
    token_header = req.headers.get("Authorization")

    if not token_header or not token_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Not authenticated")

    token = token_header.split(" ")[1]

    # STRICT REJECTION
    if token in ["null", "undefined", "", None, "None"]:
        raise HTTPException(status_code=401, detail="Invalid token")

    user = users_col.find_one({"session_token": token})
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired session token")

    return user


# ----------------------- SAVE EVENT -----------------------
@router.put("/{event_id}/save")
async def save_event(event_id: str, req: Request):
    if not ObjectId.is_valid(event_id):
        raise HTTPException(status_code=400, detail="Invalid event ID")

    user = validate_token(req)

    users_col.update_one(
        {"_id": user["_id"]},
        {"$addToSet": {"saved_events": event_id}}
    )

    return {"success": True, "saved_event_id": event_id}


# ----------------------- UNSAVE EVENT -----------------------
@router.put("/{event_id}/unsave")
async def unsave_event(event_id: str, req: Request):
    if not ObjectId.is_valid(event_id):
        raise HTTPException(status_code=400, detail="Invalid event ID")

    user = validate_token(req)

    users_col.update_one(
        {"_id": user["_id"]},
        {"$pull": {"saved_events": event_id}}
    )

    return {"success": True, "unsaved_event_id": event_id}

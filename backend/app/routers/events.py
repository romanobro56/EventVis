# app/routers/events.py
from fastapi import APIRouter
from app.models.event_models import Event, DUMMY_EVENTS

router = APIRouter(prefix="/events", tags=["events"])

@router.get("/")
def list_events():
    print("[DEBUG] Listing all events")
    return DUMMY_EVENTS

@router.get("/{event_id}")
def get_event(event_id: int):
    print(f"[DEBUG] Fetching event with ID {event_id}")
    return next((e for e in DUMMY_EVENTS if e.id == event_id), DUMMY_EVENTS[0])

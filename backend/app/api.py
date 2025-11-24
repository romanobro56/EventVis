from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

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
    # returns id of created event
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

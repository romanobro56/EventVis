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

class Event(BaseModel):
    id: int
    title: str
    description: str
    # use a different type for locations?
    location: str
    # use a different type for dates / times?
    start_time: str
    end_time: str
    # make this a user / user id instead?
    created_by: str
    # invited_users: list
    # comments: list
    # is_private: bool

DUMMY_EVENT = Event(id=0, title="title", description="description", location="location",
                    start_time="start_time", end_time="end_time", created_by="created_by")

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
    return [DUMMY_EVENT]

@app.get("/settings/")
def get_user_preferences(user_id: int):
    return {"user_id": user_id}

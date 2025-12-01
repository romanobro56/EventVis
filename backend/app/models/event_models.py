# app/models/event_models.py
from pydantic import BaseModel

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

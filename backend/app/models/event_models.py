# app/models/event_models.py
from pydantic import BaseModel

class EventModel(BaseModel):
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


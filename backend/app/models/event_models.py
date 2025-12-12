# app/models/event_models.py
from pydantic import BaseModel

class EventModel(BaseModel):
    title: str
    description: str
    full_description: str
    date: str
    start_time: str
    end_time: str
    location: str
    lat: float
    lng: float


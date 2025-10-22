from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "localhost:5173"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


"""
Each of these is a routing method;
There's one for the list view and the map view,
and I added one for specific events and user profile views.

Returns and types are just there for convenience and don't mean anything.
You can change those once this is actually implemented.
"""
@app.get("/map/")
def read_root():
    return {"Hello": "World"}

@app.get("/list/")
def read_item():
    return {"list": "list"}

@app.get("/event/{event_id}")
def get_event(event_id):
    return {"event": event_id}

@app.get("/user/{user_id}")
def get_user(user_id):
    return {"user": user_id}

"""
These are utilities, like setting and posting for actually creating an event.
This could probably be its own file, too.
"""

@app.post("/event/{event_id}")
def create_event(event_id):
    return {"event_created": event_id}

@app.get("/settings/")
def get_user_preferences(user_id):
    return {"user_id": user_id}
##this can be blank for now
##use this to define any module-wide constants
from hashlib import _Hash

# Define user classes from our JSON schemas:
class User:
    user_id: int
    name: str
    email: str
    password_hash: _Hash # Not sure if this is the right data type.

    def __init__(this, user_id: int, name: str, email: str, hash_value: _Hash):
        this.user_id = user_id
        this.name = name
        this.email = email
        this.password_hash = hash_value

# I'm not sure if we need separate JavaScript classes for these data types:
class Event:
    event_id: int
    title: str
    description: str
    location: str # This may need to be something different.
    date_time: int # Could be the number of seconds since Jan 1, 1970 midnight.
    created_by: User # Or a string?


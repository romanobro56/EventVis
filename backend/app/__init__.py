##this can be blank for now
##use this to define any module-wide constants

# Define user classes from our JSON schemas:
class User:
    user_id: str
    name: str
    email: str
    password_hash: bytes # Not sure if this is the right data type.

# I'm not sure if we need separate JavaScript classes for these data types:
class Event:
    event_id: int
    title: str
    description: str
    location: str # This may need to be something different.
    date_time: int # Could be the number of seconds since Jan 1, 1970 midnight.
    created_by: User # Or a string?


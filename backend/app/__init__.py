##this can be blank for now
##use this to define any module-wide constants
from __future__ import annotations
import hashlib

# Define user classes from our JSON schemas:
class User:
    user_id: int
    name: str
    email: str
    password_hash: hashlib._Hash # Not sure if this is the right data type.

    def __init__(this, user_id: int, name: str, email: str, hash_value):
        this.user_id = user_id
        this.name = name
        this.email = email
        this.password_hash = hash_value


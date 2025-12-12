# Define user classes from our JSON schemas:
class User:
    user_id: int
    name: str
    email: str
    password_hash: str  # <-- change from _Hash to str

    def __init__(self, user_id: int, name: str, email: str, hash_value: str):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password_hash = hash_value

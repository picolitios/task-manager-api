from datetime import datetime
from typing import Optional, Dict, Any

class UserModel:
    """
    Representation of a User document in MongoDB.
    """
    def __init__(self, email: str, hashed_password: str):
        self.email = email
        self.hashed_password = hashed_password
        self.created_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "email": self.email,
            "hashed_password": self.hashed_password,
            "created_at": self.created_at
        }
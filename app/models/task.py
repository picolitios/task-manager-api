from datetime import datetime
from typing import Optional, Dict, Any

class TaskModel:
    """
    Representation of a Task document in MongoDB.
    """
    def __init__(self, title: str, description: Optional[str] = None):
        self.title = title
        self.description = description
        self.completed = False
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        return {
            "title": self.title,
            "description": self.description,
            "completed": self.completed,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

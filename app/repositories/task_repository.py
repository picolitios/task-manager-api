from bson import ObjectId
from typing import List, Optional
from app.database.database import get_db


def serialize_task(task: dict) -> dict:
    task["id"] = str(task["_id"])
    del task["_id"]
    return task


class TaskRepository:
    def __init__(self):
        pass

    @property
    def collection(self):
        return get_db()["tasks"]

    async def create(self, task_data: dict) -> dict:
        result = await self.collection.insert_one(task_data)
        created_task = await self.collection.find_one({"_id": result.inserted_id})
        return serialize_task(created_task)

    async def get_by_id_and_owner(self, task_id: str, owner_id: str) -> Optional[dict]:
        task = await self.collection.find_one({"_id": ObjectId(task_id), "owner_id": owner_id})
        if task:
            return serialize_task(task)
        return None

    async def list_all_by_owner(self, owner_id: str, skip: int = 0, limit: int = 100) -> List[dict]:
        cursor = self.collection.find({"owner_id": owner_id}).skip(skip).limit(limit)
        tasks = await cursor.to_list(length=limit)
        return [serialize_task(task) for task in tasks]

    async def update(self, task_id: str, owner_id: str, update_data: dict) -> Optional[dict]:
        await self.collection.update_one(
            {"_id": ObjectId(task_id), "owner_id": owner_id},
            {"$set": update_data}
        )

        task = await self.collection.find_one({"_id": ObjectId(task_id), "owner_id": owner_id})
        if task:
            return serialize_task(task)
        return None

    async def delete(self, task_id: str, owner_id: str) -> bool:
        result = await self.collection.delete_one({"_id": ObjectId(task_id), "owner_id": owner_id})
        return result.deleted_count == 1
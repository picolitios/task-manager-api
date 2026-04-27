from typing import List, Optional
from datetime import datetime
from bson.errors import InvalidId
from fastapi import HTTPException, status
from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskUpdate
from app.models.task import TaskModel

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    async def create_task(self, task_data: TaskCreate) -> dict:
        task_model = TaskModel(**task_data.model_dump())
        return await self.repository.create(task_model.to_dict())

    async def get_task(self, task_id: str) -> dict:
        try:
            task = await self.repository.get_by_id(task_id)
            if not task:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
            return task
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Task ID")

    async def get_all_tasks(self, skip: int = 0, limit: int = 100) -> List[dict]:
        return await self.repository.list_all(skip, limit)

    async def update_task(self, task_id: str, task_data: TaskUpdate) -> dict:
        try:
            update_data = {k: v for k, v in task_data.model_dump(exclude_unset=True).items() if v is not None}
            if not update_data:
                raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="No data provided to update")
            
            update_data["updated_at"] = datetime.utcnow()
            
            updated_task = await self.repository.update(task_id, update_data)
            if not updated_task:
                 raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
            return updated_task
        except InvalidId:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Task ID")

    async def delete_task(self, task_id: str) -> None:
        try:
            deleted = await self.repository.delete(task_id)
            if not deleted:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        except InvalidId:
             raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid Task ID")

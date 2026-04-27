from fastapi import APIRouter, status, Depends
from typing import List
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_task_service():
    return TaskService()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(task_in: TaskCreate, service: TaskService = Depends(get_task_service)):
    return await service.create_task(task_in)

@router.get("/", response_model=List[TaskResponse])
async def read_tasks(skip: int = 0, limit: int = 100, service: TaskService = Depends(get_task_service)):
    return await service.get_all_tasks(skip=skip, limit=limit)

@router.get("/{task_id}", response_model=TaskResponse)
async def read_task(task_id: str, service: TaskService = Depends(get_task_service)):
    return await service.get_task(task_id)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(task_id: str, task_in: TaskUpdate, service: TaskService = Depends(get_task_service)):
    return await service.update_task(task_id, task_in)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(task_id: str, service: TaskService = Depends(get_task_service)):
    await service.delete_task(task_id)
    return None

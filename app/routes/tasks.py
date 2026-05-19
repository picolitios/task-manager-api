from fastapi import APIRouter, status, Depends
from typing import List
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.services.task_service import TaskService
from app.core.auth_deps import get_current_user

router = APIRouter(prefix="/tasks", tags=["Tasks"])

def get_task_service():
    return TaskService()

@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_in: TaskCreate, 
    service: TaskService = Depends(get_task_service),
    user_id: str = Depends(get_current_user)
):
    return await service.create_task(task_in, user_id)

@router.get("/", response_model=List[TaskResponse])
async def read_tasks(
    skip: int = 0, 
    limit: int = 100, 
    service: TaskService = Depends(get_task_service),
    user_id: str = Depends(get_current_user)
):
    return await service.get_all_tasks(user_id, skip=skip, limit=limit)

@router.get("/{task_id}", response_model=TaskResponse)
async def read_task(
    task_id: str, 
    service: TaskService = Depends(get_task_service),
    user_id: str = Depends(get_current_user)
):
    return await service.get_task(task_id, user_id)

@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: str, 
    task_in: TaskUpdate, 
    service: TaskService = Depends(get_task_service),
    user_id: str = Depends(get_current_user)
):
    return await service.update_task(task_id, user_id, task_in)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: str, 
    service: TaskService = Depends(get_task_service),
    user_id: str = Depends(get_current_user)
):
    await service.delete_task(task_id, user_id)
    return None

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

app = FastAPI()

# DTOs
class TaskCreateRequest(BaseModel):
    title: str
    description: Optional[str] = None
    priority: str
    assignee_id: Optional[int] = None

class TaskResponse(BaseModel):
    id: int
    title: str
    priority: str
    status: str
    created_at: datetime


# Implementación básica de TaskService
class TaskService:
    _id_counter = 1

    @classmethod
    def create_task(cls, request: TaskCreateRequest) -> TaskResponse:
        # Simula la creación de una tarea y el guardado en memoria
        task_id = cls._id_counter
        cls._id_counter += 1
        now = datetime.now()
        return TaskResponse(
            id=task_id,
            title=request.title,
            priority=request.priority,
            status="OPEN",
            created_at=now
        )

@app.post("/tasks", response_model=TaskResponse)
async def create_task(request: TaskCreateRequest):
    # El endpoint solo valida el DTO (automático por FastAPI) y llama al service
    try:
        # Ejemplo de llamada al servicio (mock)
        new_task = TaskService.create_task(request)
        return new_task
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
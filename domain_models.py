from enum import Enum
from dataclasses import dataclass
from datetime import datetime
from typing import Optional

class TaskStatus(Enum):
    OPEN = "OPEN"
    IN_PROGRESS = "IN_PROGRESS"
    DONE = "DONE"

@dataclass
class Task:
    id: Optional[int]
    title: str
    description: Optional[str]
    priority: str  # LOW, MEDIUM, HIGH
    status: TaskStatus
    assignee_id: Optional[int]
    created_at: datetime

class TaskFactory:
    @staticmethod
    def create_task(title: str, priority: str, description: str = None, assignee_id: int = None) -> Task:
        # Validar invariantes mínimos
        if not title or title.strip() == "":
            raise ValueError("El título no puede estar vacío")
        
        valid_priorities = ["LOW", "MEDIUM", "HIGH"]
        if priority not in valid_priorities:
            raise ValueError(f"Prioridad inválida. Debe ser: {valid_priorities}")

        return Task(
            id=None,
            title=title,
            description=description,
            priority=priority,
            status=TaskStatus.OPEN, # Estado inicial siempre OPEN
            assignee_id=assignee_id,
            created_at=datetime.now()
        )
from pydantic import BaseModel

from app.models.tasks import CompleteStatus


class Task(BaseModel):
    id: int
    name: str
    status: CompleteStatus
    page_id: int

    class Config:
        orm_mode = True

class TaskIn(BaseModel):
    name: str

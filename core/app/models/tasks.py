import enum
from typing import List, Optional

from sqlmodel import Enum
from sqlmodel import Field, Relationship, SQLModel, Column

from app.models.pages import Page


class CompleteStatus(str, enum.Enum):
    in_progress = 'in_progress'
    done = 'done'


class Task(SQLModel, table=True):
    __tablename__ = 'tasks'
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    name: str = Field(index=True)
    status: CompleteStatus = Field(sa_column=Column(Enum(CompleteStatus)), default=CompleteStatus.in_progress)

    page_id: Optional[int] = Field(nullable=False, foreign_key="pages.id")
    page: Optional[Page] = Relationship(back_populates="tasks")

    class Config:
        arbitrary_types_allowed = True

from sqlalchemy import Column, String, Enum, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.enum.tasks import CompleteStatus
from app.models.base import BaseModel


class Task(BaseModel):
    __tablename__ = 'tasks'
    name = Column(String(256), nullable=False)
    status: CompleteStatus = Column(Enum(CompleteStatus), default=CompleteStatus.in_progress)

    page_id = Column(Integer, ForeignKey('pages.id'), primary_key=True)
    page = relationship('Page', back_populates='tasks')

    class Config:
        arbitrary_types_allowed = True

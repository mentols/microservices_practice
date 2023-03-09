from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Page(BaseModel):
    __tablename__ = 'pages'
    name = Column(String(256), nullable=False)
    owner_id = Column(Integer, nullable=False)
    tasks = relationship('Task', back_populates='page')

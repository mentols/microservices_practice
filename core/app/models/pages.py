from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Page(BaseModel):
    __tablename__ = 'pages'
    name = Column(String(256), unique=True, nullable=False)

    tasks = relationship('Task', back_populates='page')

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.models.base import BaseModel


class Page(BaseModel):
    __tablename__ = 'pages'
    name = Column(String(256))

    tasks = relationship('Task', back_populates='page')

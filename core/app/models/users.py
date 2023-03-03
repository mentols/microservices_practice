from app.models.base import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    __tablename__ = 'users'
    username = Column(String(256), unique=True, nullable=False)
    password = Column(String(256), nullable=False)

    pages = relationship('Page', back_populates='users')

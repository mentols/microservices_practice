from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.models.base import BaseModel
from app.models.users import User


class Page(BaseModel):
    __tablename__ = 'pages'
    name = Column(String(256), unique=True, nullable=False)

    tasks = relationship('Task', back_populates='page')

    owner_id = Column(Integer, ForeignKey(User.id))
    users = relationship('User', back_populates='pages')

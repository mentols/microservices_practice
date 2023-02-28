from typing import List, Optional

from sqlmodel import Field, Relationship, SQLModel


class Page(SQLModel, table=True):
    __tablename__ = 'pages'
    id: Optional[int] = Field(default=None, primary_key=True, unique=True)
    name: str = Field(index=True)

    tasks: List["Task"] = Relationship(back_populates="page")

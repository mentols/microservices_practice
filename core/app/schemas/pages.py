from pydantic import BaseModel


class Page(BaseModel):
    id: int
    name: str


class PageIn(BaseModel):
    name: str

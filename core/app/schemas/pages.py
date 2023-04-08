from pydantic import BaseModel


class Page(BaseModel):
    id: int
    name: str
    owner_id: int

    class Config:
        orm_mode = True


class PageIn(BaseModel):
    name: str

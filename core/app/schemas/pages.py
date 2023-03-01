from pydantic import BaseModel


class Page(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class PageIn(BaseModel):
    name: str

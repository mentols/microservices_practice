from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    password: str

    class Config:
        orm_mode = True


class UserIn(BaseModel):
    username: str
    password: str


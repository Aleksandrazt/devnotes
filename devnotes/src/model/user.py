"""
Пользватели
"""

from pydantic import BaseModel


class UserBase(BaseModel):
    username: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id_: int
    username: str

    class Config:
        orm_mode = True

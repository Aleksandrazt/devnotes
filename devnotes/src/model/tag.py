"""
Тэги
"""

from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagRead(TagBase):
    id_: int
    name: str

    class Config:
        orm_mode = True

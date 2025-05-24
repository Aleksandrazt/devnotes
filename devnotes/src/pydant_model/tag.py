"""
Тэги
"""

from pydantic import BaseModel


class TagBase(BaseModel):
    name: str


class TagCreate(TagBase):
    pass


class TagUpdate(TagBase):
    name: int | None = None
    notes: int | None = None


class TagRead(TagBase):
    id_: int
    name: str

    class Config:
        orm_mode = True

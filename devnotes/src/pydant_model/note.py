"""
Для валидации заметок
"""

from datetime import datetime

from pydantic import BaseModel


class NoteBase(BaseModel):
    title: str
    content: str
    tag_id: int | None = None


class NoteCreate(NoteBase):
    pass


class NoteUpdate(NoteBase):
    title: int | None = None
    content: int | None = None
    tag_id: int | None = None


class NoteRead(NoteBase):
    id_: int
    user_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

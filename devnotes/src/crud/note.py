"""
Взаимодействие с заметиками
"""

from sqlalchemy.future import select

from devnotes.src.alchemy_schema.note import Note as NoteSchema
from devnotes.src.alchemy_schema.user import User
from devnotes.src.crud.base import BaseInteractor
from devnotes.src.custom_exception.checker import check_filter
from devnotes.src.custom_exception.constant import ID_FIELD, USER_FIELD


class Note(BaseInteractor):
    """
    Заметки
    """

    @check_filter([USER_FIELD])
    async def get_list(self, fltr: dict):
        """
        Получить список заметок
        """
        select_note = select(NoteSchema)
        for field, value in (fltr or {}).items():
            if hasattr(NoteSchema, field) and value is not None:
                select_note = select_note.where(
                    getattr(NoteSchema, field) == value
                )
        result = await self.data_base.execute(select_note)
        return result.scalars().all()

    @check_filter([USER_FIELD, ID_FIELD])
    async def get_by_id(self, fltr: dict):
        """
        Получить одну заметку по id
        """
        result = await self.data_base.execute(
            select(NoteSchema).where(
                NoteSchema.id_ == fltr.get(ID_FIELD),
                NoteSchema.author_id == fltr.get(USER_FIELD),
            )
        )
        return result.scalar_one_or_none()

    async def create(self, fltr: dict, user: User):
        """
        Создать заметку
        """
        note = NoteSchema(**fltr, author_id=user.id)
        self.data_base.add(note)
        await self.data_base.commit()
        await self.data_base.refresh(note)
        return note

    async def update(self, fltr: dict):
        """
        Обновить заметку
        """
        note = await self.get_by_id(fltr)
        if not note:
            return None
        for key, value in fltr.items():
            if not value or key in (ID_FIELD, USER_FIELD):
                continue
            setattr(note, key, value)
        await self.data_base.commit()
        await self.data_base.refresh(note)
        return note

    async def delete(self, fltr: dict):
        """
        Удалить заметку
        """
        note = await self.get_by_id(**fltr)
        if not note:
            return None
        await self.data_base.delete(note)
        await self.data_base.commit()
        return note

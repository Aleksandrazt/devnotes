"""
Взаимодействие с тегами
"""

from sqlalchemy.future import select

from devnotes.src.alchemy_schema.tag import Tag as TagSchema
from devnotes.src.crud.base import BaseInteractor
from devnotes.src.custom_exception.checker import check_filter
from devnotes.src.custom_exception.constant import ID_FIELD


class Tag(BaseInteractor):
    """
    Теги
    """

    async def get_list(self, fltr: dict):
        """
        Получить список тегов
        """
        select_note = select(TagSchema)
        for field, value in (fltr or {}).items():
            if hasattr(TagSchema, field) and value is not None:
                select_note = select_note.where(
                    getattr(TagSchema, field) == value
                )
        result = await self.data_base.execute(select_note)
        return result.scalars().all()

    @check_filter([ID_FIELD])
    async def get_by_id(self, fltr: dict):
        """
        Получить один тэг по id
        """
        result = await self.data_base.execute(
            select(
                TagSchema.where(
                    TagSchema.id_ == fltr.get(ID_FIELD),
                )
            )
        )
        return result.scalar_one_or_none()

    async def create(self, flter: dict, _):
        """
        Создать тег
        """
        tag = TagSchema(**flter)
        self.data_base.add(tag)
        await self.data_base.commit()
        await self.data_base.refresh(tag)
        return tag

    async def update(self, fltr: dict):
        """
        Обновить тег
        """
        tag = await self.get_by_id(fltr)
        if not tag:
            return None
        for key, value in fltr.items():
            if not value or key in (ID_FIELD):
                continue
            setattr(tag, key, value)
        await self.data_base.commit()
        await self.data_base.refresh(tag)
        return tag

    async def delete(self, fltr: dict):
        """
        Удалить тег
        """
        tag = await self.get_by_id(**fltr)
        if not tag:
            return None
        await self.data_base.delete(tag)
        await self.data_base.commit()
        return tag

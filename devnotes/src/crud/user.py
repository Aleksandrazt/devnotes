"""
Взаимодействие пользователями
"""

from sqlalchemy.future import select

from devnotes.src.alchemy_schema.user import User as UserSchema
from devnotes.src.crud.base import BaseInteractor
from devnotes.src.custom_exception.checker import check_filter
from devnotes.src.custom_exception.constant import ID_FIELD


class Tag(BaseInteractor):
    """
    Теги
    """

    async def get_list(self, fltr: dict):
        """
        Получить список пользователей
        """
        select_note = select(UserSchema)
        for field, value in (fltr or {}).items():
            if hasattr(UserSchema, field) and value is not None:
                select_note = select_note.where(
                    getattr(UserSchema, field) == value
                )
        result = await self.data_base.execute(select_note)
        return result.scalars().all()

    @check_filter([ID_FIELD])
    async def get_by_id(self, fltr: dict):
        """
        Получить одогго пользователя
        """
        result = await self.data_base.execute(
            select(
                UserSchema.where(
                    UserSchema.id_ == fltr.get(ID_FIELD),
                )
            )
        )
        return result.scalar_one_or_none()

    async def create(self, flter: dict, _):
        """
        Создать пользователя
        """
        user = UserSchema(**flter)
        self.data_base.add(user)
        await self.data_base.commit()
        await self.data_base.refresh(user)
        return user

    async def update(self, fltr: dict):
        """
        Обновить пользователя
        """
        user = await self.get_by_id(fltr)
        if not user:
            return None
        for key, value in fltr.items():
            if not value or key in (ID_FIELD):
                continue
            setattr(user, key, value)
        await self.data_base.commit()
        await self.data_base.refresh(user)
        return user

    async def delete(self, fltr: dict):
        """
        Удалить пользователя
        """
        user = await self.get_by_id(**fltr)
        if not user:
            return None
        await self.data_base.delete(user)
        await self.data_base.commit()
        return user

"""
Базовый интерактор с БД
"""

from sqlalchemy.ext.asyncio import AsyncSession

from devnotes.src.alchemy_schema.user import User


class BaseInteractor:
    """
    Абстрактное взаимодействие с БД
    """

    data_base: AsyncSession

    def __init__(self, data_base: AsyncSession):
        self.data_base = data_base

    async def get_list(self, fltr: dict):
        """
        Получить список данных
        """
        raise NotImplementedError()

    async def get_by_id(self, fltr: dict):
        """
        Получить один объект данных по id
        """
        raise NotImplementedError()

    async def create(self, fltr: dict, user: User):
        """
        Создать запись в БД
        """
        raise NotImplementedError()

    async def update(self, fltr: dict):
        """
        Обновить запись в БД
        """
        raise NotImplementedError()

    async def delete(self, fltr: dict):
        """
        Удалить запись в БД
        """
        raise NotImplementedError()

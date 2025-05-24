"""
Исключения в работе CRUD
"""


class NoIdInFilterException(Exception):
    """
    Исключение если нет в фильтре id
    """

    def __init__(self):
        super().__init__("При попытке получить одну запись не указано id")
        self.extra_info = (
            "При попытке получить одну запись не указано id. Проверьте фильтр."
        )


class NoUserInFilterException(Exception):
    """
    Исключение не указан пользователь
    """

    def __init__(self):
        super().__init__("Не указан пользователь")
        self.extra_info = (
            "Нельзя определить права без указания пользователя. "
            "Проверьте данные пользователя."
        )

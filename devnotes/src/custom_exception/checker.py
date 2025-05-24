"""
Валидция
"""

from devnotes.src.custom_exception.constant import FIELD_EXCEPTIONS


def check_filter(nessesrary_filds: list | None):
    """
    Проверка наличия обязательны полей в фильтре
    """

    def decorator(func):
        def wrapper(fltr, *args, **kwargs):
            for field in nessesrary_filds or []:
                if not fltr.get(field):
                    raise FIELD_EXCEPTIONS.get(
                        field, Exception(f"Не хватает поля {field}")
                    )
            return func(*args, **kwargs)

        return wrapper

    return decorator

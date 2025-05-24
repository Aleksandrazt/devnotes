"""
Константы для проверок
"""

from devnotes.src.custom_exception import crud

USER_FIELD = "author_id "
ID_FIELD = "id_"

FIELD_EXCEPTIONS = {
    USER_FIELD: crud.NoUserInFilterException,
    ID_FIELD: crud.NoIdInFilterException,
}

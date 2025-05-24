"""
Пользователи
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from devnotes.src.alchemy_schema.base import Base


class User(Base):
    __tablename__ = "users"
    id_ = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)

    notes = relationship("Note", back_populates="author")

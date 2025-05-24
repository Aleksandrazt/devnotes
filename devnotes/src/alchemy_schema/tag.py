"""
Тэги для заметок.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from devnotes.src.alchemy_schema.base import Base


class Tag(Base):
    __tablename__ = "tags"

    id_ = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)

    notes = relationship("Note", back_populates="tag")

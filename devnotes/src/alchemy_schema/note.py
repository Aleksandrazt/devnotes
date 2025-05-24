"""
Тип данных заметки
"""

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import relationship

from devnotes.src.alchemy_schema.base import Base


class Note(Base):
    __tablename__ = "notes"

    id_ = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    author = Column()

    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    author_id = Column(Integer, ForeignKey("users.id_", ondelete="CASCADE"))
    tag_id = Column(
        Integer, ForeignKey("tags.id_", ondelete="SET NULL"), nullable=True
    )

    author = relationship("User", back_populates="notes")
    tag = relationship("Tag", back_populates="notes")

import uuid
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Boolean, LargeBinary, ForeignKey
from .database import db


class Author(db.Model):
    id = Column(String(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    user_id = Column(String(length=36), ForeignKey("user.id"), nullable=False)

    user = relationship("User", back_populates="author")
    articles = relationship("Article", back_populates="author")

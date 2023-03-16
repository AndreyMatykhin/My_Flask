import uuid
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from .artical_tag import article_tag_association_table
from .database import db


class Tag(db.Model):
    id = Column(String(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    name = Column(String(32), nullable=False, default="", server_default="")

    articles = relationship("Article", secondary=article_tag_association_table, back_populates="tags",
                            )

from datetime import datetime

from sqlalchemy import Column, String, Boolean, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship

from .artical_tag import article_tag_association_table
from .database import db
import uuid


class Article(db.Model):
    id = Column(String(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    title = Column(String(80), nullable=False)
    author_id = Column(String(36), ForeignKey('author.id'))
    text = Column(String)
    dt_created = Column(DateTime, default=datetime.utcnow, server_default=func.now())
    dt_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    delete = Column(Boolean, nullable=False, default=False)
    author = relationship("Author", back_populates="articles")
    tags = relationship("Tag", secondary=article_tag_association_table, back_populates="articles",
                        )

    def __repr__(self):
        return f"<Article #{self.id} {self.title!r} {self.author!r}>"

    def __str__(self):
        return self.title

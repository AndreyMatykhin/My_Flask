from sqlalchemy import Column, String, Boolean, ForeignKey
from .database import db
import uuid


class Article(db.Model):
    id = Column(String(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    title = Column(String(80), nullable=False)
    author_id = Column(String(36), ForeignKey('user.id'))
    text = Column(String)
    author = db.relationship("User")
    delete = Column(Boolean, nullable=False, default=False)


    def __repr__(self):
        return f"<Article #{self.id} {self.title!r} {self.author!r}>"

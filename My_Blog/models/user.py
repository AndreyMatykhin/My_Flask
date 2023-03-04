from sqlalchemy import Column, String, Boolean
from sqlalchemy.orm import relationship

from .database import db
from flask_login import UserMixin
import uuid


class User(db.Model, UserMixin):
    id = Column(db.Text(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    avatar = Column(String(150), default='/static/img/default_avatar.jpg')
    is_staff = Column(Boolean, nullable=False, default=False)


    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

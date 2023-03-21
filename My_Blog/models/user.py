from sqlalchemy.orm import relationship

from ..security import flask_bcrypt
from sqlalchemy import Column, String, Boolean, LargeBinary
from .database import db
from flask_login import UserMixin
import uuid


class User(db.Model, UserMixin):
    id = Column(String(length=36), default=lambda: str(uuid.uuid4()), primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    first_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    last_name = Column(String(120), unique=False, nullable=False, default="", server_default="")
    email = Column(String(255), unique=True, nullable=False, default="", server_default="")
    avatar = Column(String(150), default='/static/img/default_avatar.jpg')
    is_staff = Column(Boolean, nullable=False, default=False)
    _password = Column(LargeBinary, nullable=False)

    author = relationship("Author", uselist=False, back_populates="user")

    def __repr__(self):
        return f"<User #{self.id} {self.username!r}>"

    def __str__(self):
        return self.username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        self._password = flask_bcrypt.generate_password_hash(value)

    def validate_password(self, password) -> bool:
        return flask_bcrypt.check_password_hash(self._password, password)

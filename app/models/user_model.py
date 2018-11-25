"""
    user模型，用于做数据库映射,继承base这个基类
"""
import uuid as uuid
from sqlalchemy import Column, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base_model import Base, db


class UserModel(Base):
    id = Column(String(32), primary_key=True)
    email = Column(String(50), unique=True, nullable=False)
    nickname = Column(String(50), unique=True)
    auth = Column(SmallInteger, default=1)
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        """
            注册新增用户
        :return:
        """
        id = str(uuid.uuid4()).replace('-', '')
        with db.auto_commit():
            user = UserModel()
            user.id = id
            user.email = account
            user.nickname = nickname
            user.password = secret
            db.session.add(user)
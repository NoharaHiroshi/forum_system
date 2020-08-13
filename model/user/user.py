# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from model.base import Base, IdGenerator


class User(Base):
    __tablename__ = 'user'

    NOT_ACTIVE, NORMAL, LOCKED = range(3)

    id = Column(BigInteger, default=IdGenerator.gen, primary_key=True)
    name = Column(String(100), index=True, nullable=False)
    password = Column(String(225), nullable=False)
    email = Column(String(100), index=True, nullable=False)
    status = Column(Integer, default=NOT_ACTIVE, index=True)

    def is_active(self):
        return self.status == User.NORMAL

    def to_dict(self):
        return {
            'id': str(self.id),
            'email': self.email,
            'name': self.name,
            'status': self.status,
            'is_active': self.is_active()
        }


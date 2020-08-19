# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from model.base import Base, IdGenerator


class Forum(Base):
    __tablename__ = 'forum'

    OPEN, CLOSED, HIDDEN = range(3)

    id = Column(BigInteger, default=IdGenerator.gen, primary_key=True)
    name = Column(String(100), index=True, nullable=False)
    status = Column(Integer, index=True, default=OPEN)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "status": self.status,
            "created_date": self.created_date.strftime('%Y-%m-%d %H:%M'),
            "modified_date": self.modified_date.strftime('%Y-%m-%d %H:%M')
        }


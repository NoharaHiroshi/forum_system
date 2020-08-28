# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from model.base import Base, IdGenerator


class Post(Base):
    __tablename__ = 'post'

    DRAFT, CHECKING, PASS, NOT_PASS, DELETED, HIDDEN = range(5)

    id = Column(BigInteger, default=IdGenerator.gen, primary_key=True)
    sub_forum_id = Column(BigInteger, index=True, nullable=False)
    user_id = Column(BigInteger, index=True, nullable=False)
    title = Column(String(100), index=True, nullable=False)
    status = Column(Integer, index=True, default=DRAFT)
    cost = Column(Integer, index=True, nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "sub_forum_id": str(self.sub_forum_id),
            "user_id": str(self.user_id),
            "title": self.title,
            "status": self.status,
            "cost": self.cost,
            "created_date": self.created_date.strftime('%Y-%m-%d %H:%M'),
            "modified_date": self.modified_date.strftime('%Y-%m-%d %H:%M')
        }

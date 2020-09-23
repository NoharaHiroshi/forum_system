# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from model.base import Base, IdGenerator


class UserPayRecord(Base):
    __tablename__ = 'user_pay_record'

    id = Column(BigInteger, default=IdGenerator.gen, primary_key=True)
    user_id = Column(BigInteger, index=True, nullable=False)
    post_id = Column(BigInteger, index=True, nullable=False)
    cost = Column(BigInteger, index=True, nullable=False)

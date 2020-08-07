# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from model.base import Base, IdGenerator


class Role(Base):
    __tablename__ = 'role'

    NORMAL, CLOSED = range(2)

    id = Column(BigInteger, default=IdGenerator.gen, primary_key=True)
    name = Column(String(100), index=True, nullable=False)
    status = Column(Integer, default=NORMAL, index=True)

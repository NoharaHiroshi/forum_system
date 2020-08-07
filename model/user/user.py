# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from model.base import Base, IdGenerator


class User(Base):
    __tablename__ = 'user'

    UNKNOWN, BOY, GIRL = range(3)

    NORMAL, LOCKED = range(2)

    id = Column(BigInteger, default=IdGenerator.gen, primary_key=True)
    name = Column(String(100), index=True, nullable=False)
    password = Column(String(225), nullable=False)
    sex = Column(Integer, default=UNKNOWN, index=True)
    phone = Column(BigInteger, index=True, nullable=False)
    email = Column(String(100), index=True, nullable=False)
    status = Column(Integer, default=NORMAL, index=True)


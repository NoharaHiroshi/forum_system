# coding=utf-8

from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from model.base import Base, IdGenerator


class UserRoleRel(Base):
    __tablename__ = 'user_role_rel'

    id = Column(BigInteger, default=IdGenerator.gen, primary_key=True)
    user_id = Column(BigInteger, index=True, nullable=False)
    role_id = Column(BigInteger, index=True, nullable=False)

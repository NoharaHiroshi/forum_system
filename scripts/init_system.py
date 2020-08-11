# coding=utf-8

from model.base import IdGenerator
from model.config.session import *
from model.user.user import *
from model.user.role import *
from model.user.user_role_rel import *
from libs.aes_chiper import *


# 1、建表
def create_tables():
    Base.metadata.create_all(engine)


# 2、初始化系统时运行，用以设定管理员及会员等级
def init_system_config(name, email, password):
    with get_session() as db_session:
        # 初始化管理员
        user_id = IdGenerator.gen()
        user = User()
        user.id = user_id
        user.name = name
        user.email = email
        user.password = AESCipher.encrypt(password)
        db_session.add(user)
        # 初始化角色
        role_id = IdGenerator.gen()
        role = Role()
        role.id = role_id
        role.name = u"管理员"
        db_session.add(role)
        # 关联关系
        user_role_rel = UserRoleRel()
        user_role_rel.role_id = role_id
        user_role_rel.user_id = user_id
        db_session.add(user_role_rel)
        db_session.commit()


if __name__ == "__main__":
    # create_tables()
    init_system_config("Lands", "380788433@qq.com", "LanziDuola_LJK")

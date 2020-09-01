# coding=utf-8

from model.base import IdGenerator
from model.config.session import *
from model.user.user import *
from model.user.role import *
from model.user.user_role_rel import *
from model.forum.forum import *
from model.forum.sub_forum import *
from model.forum.forum_category import *
from model.forum.forum_sub_category import *
from model.forum.post_category_rel import *
from model.forum.post import *
from model.common.image import Image
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


# 3、创建论坛模块
def create_forum(forum_name, sub_forum_list):
    with get_session() as db_session:
        forum = db_session.query(Forum).filter(
            Forum.name == forum_name
        ).first()
        if not forum:
            forum_id = IdGenerator.gen()
            forum = Forum()
            forum.id = forum_id
            forum.name = forum_name
            db_session.add(forum)
        else:
            forum_id = forum.id
        for sub_forum_name in sub_forum_list:
            sub_forum = SubForum()
            sub_forum.forum_id = forum_id
            sub_forum.name = sub_forum_name
            db_session.add(sub_forum)
        db_session.commit()


# 4、创建论坛分类
def create_forum_category(sub_forum_name, category_name, sub_category_list):
    with get_session() as db_session:
        sub_forum = db_session.query(SubForum).filter(
            SubForum.name == sub_forum_name
        ).first()
        if sub_forum:
            sub_forum_id = sub_forum.id
            forum_category = db_session.query(ForumCategory).filter(
                ForumCategory.name == category_name
            ).first()
            if not forum_category:
                category_id = IdGenerator.gen()
                forum_category = ForumCategory()
                forum_category.id = category_id
                forum_category.name = category_name
                forum_category.sub_forum_id = sub_forum_id
                db_session.add(forum_category)
            else:
                category_id = forum_category.id
            for sub_category_name in sub_category_list:
                sub_category = db_session.query(ForumSubCategory).filter(
                    ForumSubCategory.name == sub_category_name
                ).first()
                if not sub_category:
                    sub_category = ForumSubCategory()
                    sub_category.category_id = category_id
                    sub_category.name = sub_category_name
                    db_session.add(sub_category)
        db_session.commit()


if __name__ == "__main__":
    create_tables()
    # init_system_config("Lands", "380788433@qq.com", "12345678")
    # create_forum("资源中心", ["漫画资源"])
    # create_forum_category("漫画资源", "类型", ["冒险", "热血", "搞笑", "恋爱", "少女", "日常", "校园", "运动", "治愈", "玄幻", "奇幻", "恐怖", "悬疑", "推理"])

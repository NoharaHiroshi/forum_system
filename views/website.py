# coding=utf-8

import traceback
from flask import Blueprint, jsonify, abort, request
from model.config.session import get_session
from model.forum.forum import Forum
from model.forum.sub_forum import SubForum
from model.forum.forum_category import ForumCategory
from model.forum.forum_sub_category import ForumSubCategory

website = Blueprint('website', __name__, static_folder='templates')


@website.route('/index', methods=['GET'])
def forum_list():
    try:
        result = {
            'response': 'success',
            "forum_list": list(),
            "info": ""
        }
        with get_session() as db_session:
            forums = db_session.query(Forum).all()
            if len(forums):
                for forum in forums:
                    forum_dict = forum.to_dict()
                    sub_forum_list = db_session.query(SubForum).filter(
                        SubForum.forum_id == forum.id
                    ).all()
                    forum_dict["sub_forums"] = list()
                    if len(sub_forum_list):
                        for sub_forum in sub_forum_list:
                            sub_forum_dict = sub_forum.to_dict()
                            forum_dict["sub_forums"].append(sub_forum_dict)
                    result["forum_list"].append(forum_dict)
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)


@website.route('/forum', methods=['GET'])
def forum_info():
    try:
        result = {
            'response': 'success',
            "category_list": list(),
            "info": ""
        }
        sub_forum_id = request.args.get("sub_forum_id", None)
        with get_session() as db_session:
            sub_forum = db_session.query(SubForum).filter(
                SubForum.id == sub_forum_id
            ).first()
            if sub_forum:
                forum_categories = db_session.query(ForumCategory).filter(
                    ForumCategory.sub_forum_id == sub_forum_id
                ).all()
                if len(forum_categories):
                    for forum_category in forum_categories:
                        forum_category_dict = forum_category.to_dict()
                        forum_sub_categories = db_session.query(ForumSubCategory).filter(
                            ForumSubCategory.category_id == forum_category.id
                        ).all()
                        if len(forum_sub_categories):
                            forum_category_dict["sub_categories"] = list()
                            for forum_sub_category in forum_sub_categories:
                                forum_category_dict["sub_categories"].append(forum_sub_category.to_dict())
                        result["category_list"].append(forum_category_dict)
            else:
                result.update({
                    'response': 'fail',
                    "info": "当前论坛不存在"
                })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)

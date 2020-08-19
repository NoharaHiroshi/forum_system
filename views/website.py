# coding=utf-8

import traceback
from flask import Blueprint, jsonify, abort
from model.config.session import get_session
from model.forum.forum import Forum
from model.forum.sub_forum import SubForum

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


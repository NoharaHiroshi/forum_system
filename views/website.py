# coding=utf-8

import traceback
from flask_login import current_user
from flask import Blueprint, jsonify, abort, request
from model.config.session import get_session
from model.forum.forum import Forum
from model.user.user import User
from model.forum.sub_forum import SubForum
from model.forum.forum_category import ForumCategory
from model.forum.forum_sub_category import ForumSubCategory
from model.forum.post import Post
from model.common.image import Image

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
            "post_list": list(),
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
                all_post = db_session.query(Post, User, Image).join(
                    User, User.id == Post.user_id
                ).join(
                    Image, Image.id == Post.cover_image_id
                ).filter(
                    Post.status == Post.PASS,
                    Post.sub_forum_id == sub_forum_id
                ).order_by(-Post.created_date).all()
                if len(all_post) > 0:
                    for post, user, image in all_post:
                        post_dict = post.to_dict()
                        post_dict["user"] = user.name
                        post_dict["cover_image_url"] = image.get_image_url()
                        result["post_list"].append(post_dict)
            else:
                result.update({
                    'response': 'fail',
                    "info": "当前论坛不存在"
                })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)


@website.route('/edit_post', methods=['GET'])
def edit_post():
    try:
        result = {
            "response": "success",
            "info": ""
        }
        sub_forum_id = request.args.get("sub_forum_id", None)
        with get_session() as db_session:
            post = db_session.query(Post).filter(
                Post.user_id == current_user.id,
                Post.sub_forum_id == sub_forum_id,
                Post.status == Post.DRAFT
            ).first()
            if post:
                image = db_session.query(Image).get(post.cover_image_id)
                post_data = post.to_dict()
                post_data["hidden_content"] = post.get_hidden_content()
                post_data["cover_image_url"] = image.get_image_url() if image else ""
                post_data["content"] = post.get_content()
                result.update({
                    "data": post_data
                })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)


@website.route('/submit_post', methods=['POST'])
def submit_post():
    try:
        result = {
            'response': 'success',
            "info": ""
        }
        post_id = request.json.get("post_id", None)
        sub_forum_id = request.json.get("sub_forum_id", None)
        title = request.json.get("title", None)
        content = request.json.get("content", None)
        hidden_content = request.json.get("hidden_content", None)
        cover_image_id = request.json.get("cover_image_id", None)
        cost = request.json.get("cost", 0)
        status = request.json.get("status", 0)
        if status not in [Post.DRAFT, Post.CHECKING]:
            result.update({
                'response': 'fail',
                "info": "当前提交帖子状态错误"
            })
            return jsonify(result)
        with get_session() as db_session:
            sub_forum = db_session.query(SubForum).filter(
                SubForum.id == sub_forum_id
            ).first()
            if sub_forum:
                if post_id:
                    post = db_session.query(Post).filter(
                        Post.user_id == current_user.id,
                        Post.id == post_id
                    ).first()
                    if post:
                        post.title = title
                        post.status = status
                        post.content = content
                        post.cover_image_id = cover_image_id
                        post.hidden_content = hidden_content
                        post.cost = cost
                    else:
                        result.update({
                            'response': 'fail',
                            "info": "当前提交不存在"
                        })
                        return jsonify(result)
                else:
                    post = Post()
                    post.sub_forum_id = sub_forum_id
                    post.user_id = current_user.id,
                    post.title = title
                    post.status = status
                    post.content = content
                    post.cover_image_id = cover_image_id
                    post.hidden_content = hidden_content
                    post.cost = cost
                    db_session.add(post)
                db_session.commit()
                post_data = post.to_dict()
                result.update({
                    "data": post_data
                })
            else:
                result.update({
                    'response': 'fail',
                    "info": "当前论坛不存在"
                })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)
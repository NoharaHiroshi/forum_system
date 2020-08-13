# coding=utf-8

import traceback
from model.config.session import get_session
from sqlalchemy import or_
from model.user.user import User
from flask import Blueprint, request, jsonify, abort
from libs.aes_chiper import AESCipher
from libs.gen_captcha import Captcha
from redis_store import redis_db

user = Blueprint('user', __name__, static_folder='templates')


def get_token_id_key(token_id):
    return "tokenId_%s" % token_id


@user.route('/checkUserNameValid', methods=['POST'])
def check_user_name_valid():
    try:
        result = {
            'response': 'success',
            'info': ''
        }
        name = request.json.get("name", None)
        with get_session() as db_session:
            user = db_session.query(User).filter(
                User.name == name
            ).first()
            if user:
                result.update({
                    "response": "fail",
                    "info": "当前用户名已存在"
                })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)


@user.route('/checkUserEmailValid', methods=['POST'])
def check_user_email_valid():
    try:
        result = {
            'response': 'success',
            'info': ''
        }
        email = request.json.get("email", None)
        with get_session() as db_session:
            user = db_session.query(User).filter(
                User.email == email
            ).first()
            if user:
                result.update({
                    "response": "fail",
                    "info": "当前用户邮箱已存在"
                })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)


@user.route('/register', methods=['POST'])
def register():
    try:
        result = {
            'response': 'success',
            'info': ''
        }
        name = request.json.get("name", None)
        password = request.json.get("password", None)
        email = request.json.get("email", None)
        if None in [name, password, email]:
            result.update({
                "response": "fail",
                "info": "请求参数错误"
            })
            return jsonify(result)
        en_password = AESCipher.encrypt(password),
        with get_session() as db_session:
            u = db_session.query(User).filter(
                or_(User.name == name, User.email == email)
            ).first()
            if u:
                result.update({
                    "response": "fail",
                    "info": "当前用户已存在"
                })
                return jsonify(result)
            else:
                u = User()
                u.name = name
                u.password = en_password
                u.email = email
                db_session.add(u)
                db_session.commit()
                return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)


@user.route('/getCaptcha', methods=['POST'])
def get_captcha():
    try:
        result = {
            'response': 'success',
            'data': '',
            'info': ''
        }
        token_id = request.json.get("tokenId", None)
        img, s = Captcha.get_captcha()
        result["data"] = "data:image/jpg;base64," + img
        redis_db.set(get_token_id_key(token_id), s, 300)
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)


@user.route('/login', methods=['POST'])
def login():
    try:
        result = {
            'response': 'success',
            'info': ''
        }
        token_id = request.json.get("tokenId", None)
        password = request.json.get("password", None)
        email = request.json.get("email", None)
        captcha = request.json.get("captcha", None)
        if None in [password, email, captcha]:
            result.update({
                "response": "fail",
                "info": "请求参数错误"
            })
            return jsonify(result)
        store_captcha = str(redis_db.get(get_token_id_key(token_id)), "utf-8")
        if store_captcha != captcha.upper():
            result.update({
                "response": "fail",
                "info": "验证码输入错误"
            })
            return jsonify(result)
        with get_session() as db_session:
            u = db_session.query(User).filter(
                User.email == email
            ).first()
            if u:
                de_password = AESCipher.decrypt(u.password)
                if de_password != password:
                    result.update({
                        "response": "fail",
                        "info": "密码输入错误"
                    })
                    return jsonify(result)
                else:
                    return jsonify(result)
            else:
                result.update({
                    "response": "fail",
                    "info": "当前用户不存在"
                })
                return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)

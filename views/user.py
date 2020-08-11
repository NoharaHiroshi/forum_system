# coding=utf-8

import traceback
from model.config.session import get_session
from sqlalchemy import or_
from model.user.user import User
from flask import Blueprint, request, jsonify, abort
from libs.aes_chiper import AESCipher

user = Blueprint('user', __name__, static_folder='templates')


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
                    "info": "current user name has already exist"
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
                    "info": "current user email has already exist"
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
                "info": "params not enough"
            })
            return jsonify(result)
        en_password = AESCipher.encrypt(password),
        with get_session() as db_session:
            user = db_session.query(User).filter(
                or_(User.name == name, User.email == email)
            ).first()
            if user:
                result.update({
                    "response": "fail",
                    "info": "current user name has already exist"
                })
                return jsonify(result)
            else:
                user = User()
                user.name = name
                user.password = en_password
                user.email = email
                db_session.add(user)
                db_session.commit()
                return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)


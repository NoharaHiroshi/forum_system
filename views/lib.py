# coding=utf-8

import os
import traceback
from model.config.session import get_session
from model.common.image import Image
from model.base import IdGenerator
from flask import Blueprint, request, jsonify, abort

lib = Blueprint('lib', __name__, static_folder='templates')


@lib.route('/upload_image', methods=['POST'])
def upload_image():
    result = {
        'response': 'success',
        "info": ""
    }
    try:
        img = request.files.get("img", None)
        if img:
            img_dict = Image.upload_image(img)
            result.update({
                "data": img_dict
            })
        else:
            result.update({
                'response': 'fail',
                "info": "请上传图片"
            })
        return jsonify(result)
    except Exception as e:
        print(traceback.format_exc(e))
        abort(500)
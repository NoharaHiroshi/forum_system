# coding=utf-8

import os
import datetime
from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, Float
from model.base import Base, IdGenerator
from model.config.session import get_session
from PIL import Image as Img

UPLOAD_SRC = os.path.join(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "static"), "image")


class Image(Base):
    __tablename__ = 'image'

    NORMAL, DELETED = range(2)

    id = Column(BigInteger, default=IdGenerator.gen, primary_key=True)
    name = Column(String(200))
    status = Column(Integer, index=True, default=NORMAL)
    width = Column(Integer, index=True, nullable=False)
    height = Column(Integer, index=True, nullable=False)
    path = Column(String(100), nullable=False)

    def to_dict(self):
        return {
            "id": str(self.id),
            "name": self.name,
            "status": self.status,
            "width": self.width,
            "height": self.height,
            "image_url": self.get_image_url()
        }

    def get_image_url(self):
        return os.path.join(self.path, self.name).replace('\\', '/')

    @classmethod
    def upload_image(cls, img_obj):
        with get_session() as db_session:
            img_id = str(IdGenerator.gen())
            path_src = datetime.datetime.now().strftime('%Y-%m-%d')
            upload_src = os.path.join(UPLOAD_SRC, path_src)
            if not os.path.exists(upload_src):
                os.makedirs(upload_src)
            im = Img.open(img_obj)
            width, height = im.size
            file_format = im.format
            file_name = '.'.join([img_id, file_format.lower()])
            file_full_path = os.path.join(upload_src, file_name).replace('\\', '/')
            im.save(file_full_path)
            # 数据库存储
            img = Image()
            img.id = img_id
            img.name = file_name
            img.width = width
            img.height = height
            img.path = path_src
            img.status = cls.NORMAL
            db_session.add(img)
            img_dict = img.to_dict()
            img_dict["src"] = os.path.join(path_src, file_name).replace('\\', '/')
            db_session.commit()
        return img_dict

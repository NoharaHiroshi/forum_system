# coding=utf-8

from redis_store import config
from redis_store.redis_cahce import RedisCache

# 默认通用缓存,  可以设置对象，列表, 字典等
redis_db = RedisCache(config.REDIS_CACHES['default'])

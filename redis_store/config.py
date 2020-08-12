# coding=utf-8

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

# Session
REDIS_CACHE_DB = 0

REDIS_CACHES={
    'default': {
        'HOST' : REDIS_HOST,
        'PORT' : REDIS_PORT,
        'DB' : REDIS_CACHE_DB,
        'TIMEOUT': 3600 * 24 * 7,
    },
}
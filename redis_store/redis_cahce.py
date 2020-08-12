# coding=utf-8

import redis
import zlib
import pickle


class RedisCache(object):
    def __init__(self, params={}):
        default_timeout = 3600 * 24 * 100
        host = params.get('HOST', '127.0.0.1')
        port = params.get('PORT', 6379)
        db = params.get('DB', 0)
        timeout = params.get('timeout', params.get('TIMEOUT', default_timeout))
        if timeout is not None:
            try:
                timeout = int(timeout)
            except (ValueError, TypeError):
                timeout = 300
        self.default_timeout = timeout

        self._cache = redis.StrictRedis(host=host, port=port, db=db)
        self._headers = {'zlib': '!zlib!', 'pickle': '!pickle!'}

    def _prepare_key(self, raw_key):
        return str(raw_key)
        # return smart_str(raw_key)

    def _check_header(self, header, value):
        header_marker = self._headers.get(header)
        if header_marker and \
                isinstance(value, str) and \
                value[:len(header_marker)] == header_marker:
            value = value[len(header_marker):]
            if header == 'zlib':
                value = zlib.decompress(value)
            if header == 'pickle':
                value = pickle.loads(value)
        return value

    def _pack_value(self, value):
        if isinstance(value, str):
            pass
        elif isinstance(value, int) or isinstance(value, float):
            value = str(value)
        else:
            value = self._headers['pickle'] + pickle.dumps(value)
        # zlib.compress if value is long enough
        if len(value) > 1000:
            value = self._headers['zlib'] + zlib.compress(value)
        return value

    def _unpack_value(self, value):
        value = self._check_header('zlib', value)
        value = self._check_header('pickle', value)
        return value

    def add(self, key, value, timeout=0):
        if self._cache.exists(key):
            return False
        return self.set(key, value, timeout or self.default_timeout)

    def set(self, key, value, timeout=None):
        key = self._prepare_key(key)

        # store the key/value pair
        result = self._cache.set(key, self._pack_value(value))

        # set content expiration, if necessary
        self._cache.expire(key, timeout or self.default_timeout)

        return result

    def get(self, key, default=None):
        key = self._prepare_key(key)
        value = self._cache.get(key)

        if value is None:
            return default
        else:
            return self._unpack_value(value)

    def incr(self, key, amount):
        return self._cache.incr(key, amount)

    def decr(self, key, amount):
        return self._cache.decr(key, amount)

    def delete(self, key):
        key = self._prepare_key(key)
        self._cache.delete(key)

    def expire(self, key, time):
        self._cache.expire(key, time)

    def flush(self, all_dbs=False):
        self._cache.flush(all_dbs)

    def close(self, **kwargs):
        pass

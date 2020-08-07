# coding=utf-8

"""开发环境使用的配置
"""

DB_DEBUG = False
DB = 'forum_system'
HOST = ''
USER = ''
PASSWORD = ''
CONNECT_STRING = 'mysql+pymysql://%s:%s@%s/%s?charset=utf8' % (USER, PASSWORD, HOST, DB)

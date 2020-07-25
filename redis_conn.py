# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 22:38
# @Author  : CC
# @Desc    : RedisConnection.py
import redis
from pypattyrn.structural.flyweight import FlyweightMeta
from redis import Redis


class RedisConn(Redis, metaclass=FlyweightMeta):
    """
    redis连接享元模式无需担心重复创建连接
    """
    pass


if __name__ == '__main__':
    redis_host = '127.0.0.1'
    redis_port = 6379
    redis_db = 0
    password = ''
    redis1 = RedisConn(host=redis_host, port=redis_port, db=redis_db, password=password)
    redis2 = RedisConn(host=redis_host, port=redis_port, db=redis_db, password=password)
    print(id(redis1) == id(redis2))
    redis3 = RedisConn(host=redis_host, port=redis_port, db=1, password=password)
    print(id(redis1) == id(redis3))
    redis1.set('t', 1)
    print(redis1.get('t'))

# -*- coding:utf-8 -*-
# @Author cc
# @TIME 2019/11/18 22:41
# @DESC redis工具类

import redis

ip = ''
password = ''
exper_seconds = 60 * 60
redis_port = 6379
redis_db = 0


def get_conn():
    if hasattr(get_conn, 'r'):
        return get_conn.r
    else:
        if password:
            pool = redis.ConnectionPool(host=ip, port=redis_port, db=redis_db, password=password)
        else:
            pool = redis.ConnectionPool(host=ip, port=redis_port, db=redis_db)
        get_conn.r = redis.Redis(connection_pool=pool)
        return get_conn.r


def set_value(key, value):
    return get_conn().setex(key, value, exper_seconds)


def set_value_exper(key, value, seconds):
    return get_conn().setex(key, value, seconds)


def set_value_notexper(key, value):
    return get_conn().set(key, value)


def incr_key(key):
    return get_conn().incr(key, 1)


def get_value(key):
    result = get_conn().get(key)
    if isinstance(result, bytes):
        result = result.decode('utf-8')
    return result


def getm_value(keys):
    return get_conn().mget(keys)


def quenen_push(quenen_name, value):
    """
    队列写入数据
    :param quenen_name: 队列名
    :param value: 写入值
    :return:
    """
    get_conn().lpush(quenen_name, value)


def quenen_pop(quenen_name):
    """
    获取指定队列数据
    :param quenen_name: 队列名称
    :return: 队列中取出来的值
    """
    return get_conn().rpop(quenen_name)


def get_hash_vale(key):
    return get_conn().hgetall(key)


def zadd_element(sortset_name, value, socre):
    result = get_conn().zadd(sortset_name, value, socre)
    get_conn().expire(sortset_name, exper_seconds)
    return True if result > 0 else False


def zrange_element_withscores(sortset_name, begin, end):
    return get_conn().zrange(sortset_name, begin, end, withscores=True)


def zrange_element_value(sortset_name, begin, end):
    return get_conn().zrange(sortset_name, begin, end)


def hset_field(name, key, value):
    get_conn().hset(name, key, value)
    get_conn().expire(name, exper_seconds)


def delte_field(name, key):
    return get_conn().hdel(name, key)


def hget_field(name, key):
    result = get_conn().hget(name, key)
    if result:
        result = result.decode('utf-8')
    return result


def smembers(name):
    return get_conn().smembers(name)


def check_value_inset(setname, value):
    return get_conn().sismember(setname, value)


def sadd(name, value):
    get_conn().sadd(name, value)
    get_conn().expire(name, exper_seconds)


def sadd_list(name, value:list):
"""
往redis set集合中添加多条记录
:param name: 集合名称
:param value: 列表值
:return: None
"""
if value:
    get_conn().sadd(name, *set(value))
    get_conn().expire(name, exper_seconds)


def sadd_not_expire(name, value):
    get_conn().sadd(name, value)


def hget_fields(name, keys):
    """
    获取hashmap键值多个键值对
    """
    return get_conn().hmget(name, keys)


def check_key_exists(key):
    return get_conn().exists(key)


def set_value_nx(name, value):
    """
    分布式锁设值
    :param name:属性名
    :param value:属性值
    :return: 如果存在这个键值，就返回False，否则返回True
    """
    result = get_conn().setnx(name, value)
    if result:
        get_conn().expire(name, exper_seconds)
    return result


def delete_key(key):
    return get_conn().delete(key)


if __name__ == '__main__':
    set_value('test1', '中国')
    print(get_value('test1'))
    print(set_value_nx('test2', '中国'))
    set_value_exper('test5', 'bbbb', 30)
    set_value_notexper('test6', 'ccc')
    print(incr_key('test7'))
    print(getm_value(['test1', 'test3']))
    quenen_push('test_queue', 123456)
    print(quenen_pop('test_queue'))
    hset_field('ht', 'field1', 333)
    hset_field('ht', 'field2', 555)
    delte_field('ht', 'field2')
    print(get_hash_vale('ht'))
    print(hget_field('ht', 'field1'))
    sadd('test8', 1)
    sadd_list('test8', [2, 3, 4, 5, 6])
    print(smembers('test8'))
    print(check_value_inset('test8', 1))
    delete_key('test8')
    zadd_element('test9', 'tr1', 1)
    zadd_element('test9', 'tr2', 2)
    zadd_element('test9', 'tr3', 3)
    print(zrange_element_withscores('test9', 0, 2))
    print(zrange_element_value('test9', 0, 2))

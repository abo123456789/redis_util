
redis操作工具类

### 安装依赖:

```shell
pip install -r requirements.txt
```



### 使用实例


```python
    set_value('test1', '中国')
    print(get_value('test1'))
    print(set_value_nx('test2', '中国'))
    set_value_exper('test5', 'bbbb', 30)
    set_value_notexper('test6', 'ccc')
    print(incr_key('test7'))
    print(getm_value(['test1','test3']))
    quenen_push('test_queue',123456)
    print(quenen_pop('test_queue'))
    hset_field('ht', 'field1', 333)
    hset_field('ht', 'field2', 555)
    delte_field('ht', 'field2')
    print(get_hash_vale('ht'))
    print(hget_field('ht', 'field1'))
    sadd('test8', 1)
    sadd_list('test8', [2,3,4,5,6])
    print(smembers('test8'))
    print(check_value_inset('test8', 1))
    delete_key('test8')
    zadd_element('test9', 'tr1', 1)
    zadd_element('test9', 'tr2', 2)
    zadd_element('test9', 'tr3', 3)
    print(zrange_element_withscores('test9',0,2))
    print(zrange_element_value('test9',0,2))

```

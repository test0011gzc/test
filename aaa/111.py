# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""
import pymysql

tables = ['mch_info_front', 'mch_info', 'mch_pre_info', 'mch_pre_img']
# tables = ['mch_pre_img']
test_mysql_conn = pymysql.connect(host="112.74.105.10", password="Qaz123", user="zhengxiaowen", database="dh_pay_2",
                                  port=3306)
nomal_mysql_conn = pymysql.connect(host="124.156.181.186", password="dspread@mgr", user="root", database="dh_pay",
                                   port=3306)


def test(cursor,nomal=0):
    a = []
    e = []
    cursor.execute('show create table %s;' % table)
    x = cursor.fetchone()
    if nomal == 1:
        print('这是正式数据库%s表的ddl。。。。' % table)
    else:
        print('这是测试数据库%s表的ddl。。。。' % table)
    print(x)
    # for i in x:
    #     y = i.split('\n')[1:]
    #     for z in y:
    #         if z == [] or '':
    #             continue
    #         a.append(z.strip().split(' '))
    # for i in a[:-1]:
    #     s = ''
    #     for b in i:
    #         s += ' ' + b
    #     e.append(s.lstrip()[:-1])
    # # print(e)
    # return e


for table in tables:

    diff = []
    test_cursor = test_mysql_conn.cursor()
    nomal_cursor = nomal_mysql_conn.cursor()
    nomal_list = test(nomal_cursor,nomal=1)
    # print('======================================')
    test_list = test(test_cursor,nomal=0)
    # for p in nomal_list:
    #     # print(p)
    #     if p not in test_list:
    #         print(p)
    #         diff.append(p)
    # print('这是%s新表和旧表的不同'%table)
    # print(diff)
    # print('正在查新下一张表')

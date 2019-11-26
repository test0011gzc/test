# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""
import pymysql
tables = ['mch_info_front','mch_info','mch_pre_info','mch_pre_img']
# tables = ['mch_pre_img']
test_mysql_conn = pymysql.connect(host="112.74.105.10",password="Qaz123",user="zhengxiaowen",database="dh_pay_2",port=3306)
nomal_mysql_conn = pymysql.connect(host="124.156.181.186",password="dspread@mgr",user="root",database="dh_pay",port=3306)

cursor = nomal_mysql_conn.cursor()

for table in tables:
    a = []
    e = []
    cursor.execute('show create table %s;'%table)
    x = cursor.fetchone()
    print('这是%s表的ddl。。。。'%table)
    for i in x:
        y = i.split('\n')[1:]
        for z in y:
            if z == [] or '':
                continue
            a.append(z.strip().split(' '))
    for i in a[:-1]:
        s = ''
        for b in i:
            s += ' '+b
        e.append(s)
    print(e)

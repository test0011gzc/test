# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""
import MySQLdb
import traceback
from DBUtils.PooledDB import PooledDB



g_erp_db_pool = None
def ksher_get_db_conn():
    global g_erp_db_pool
    if not g_erp_db_pool:
        g_erp_db_pool = PooledDB(MySQLdb, base_config['MYSQL_POOL_SIZE'],
                                 host=base_config['MYSQL_HOST_ERP'],
                                 user=base_config['MYSQL_USER_ID_ERP'],
                                 passwd=base_config['MYSQL_PASSWORD_ERP'],
                                 db=base_config['ERP_DATABASE_NAME_ERP'],
                                 port=int(base_config['MYSQL_PORT_ERP']),
                                 charset='utf8')  # 5为连接池里的最少连接数
    return g_erp_db_pool.connection()

g_settlement_db_pool = None
def settlement_get_db_conn():
    global g_settlement_db_pool
    if not g_settlement_db_pool:
        g_settlement_db_pool = PooledDB(MySQLdb, base_config['MYSQL_POOL_SIZE'],
                                        host=base_config['MYSQL_HOST_SETTLEMENT'],
                                        user=base_config['MYSQL_USER_ID_SETTLEMENT'],
                                        passwd=base_config['MYSQL_PASSWORD_SETTLEMENT'],
                                        db=base_config['ERP_DATABASE_NAME_SETTLEMENT'],
                                        port=int(base_config['MYSQL_PORT_SETTLEMENT']),
                                        charset='utf8')  # 5为连接池里的最少连接数
    return g_settlement_db_pool.connection()

class ConnectionPool(object):
    """
    数据库连接种类
    """
    ERP = "ERP"
    PAY = "PAY"
    SETTLEMENT = "SETTLEMENT"


class SQLHelper(object):
    """
    数据库操作帮助类
    """
    @classmethod
    def select_one(cls, sql, args=None, connection_flag=ConnectionPool.ERP):
        try:
            conn = ksher_get_db_conn()
            if connection_flag == ConnectionPool.ERP:
                conn = ksher_get_db_conn()
            if connection_flag == ConnectionPool.SETTLEMENT:
                conn = settlement_get_db_conn()
            cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            arguments_string = " arg: %s" % str(args) if args else ''
            print("-----SQL: " + sql)
            if arguments_string:
                print("#####Params: " + arguments_string)
            db_item = cursor.fetchone()
            return db_item
        except Exception as e:
            print("-----SQL数据库错误代码: {}, {}".format(e.args[0], e.args[1]))
            print("-----SQL: %s, 参数: %s", str(sql), str(args))
            print('-----SQL具体错误: ' + traceback.format_exc())
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @classmethod
    def select_all(cls, sql, args=None, connection_flag=ConnectionPool.ERP):
        try:
            if connection_flag == ConnectionPool.ERP:
                conn = ksher_get_db_conn()
            if connection_flag == ConnectionPool.SETTLEMENT:
                conn = settlement_get_db_conn()
            cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            # final_sql = sql
            if args:
                cursor.execute(sql, args)
            else:
                cursor.execute(sql)
            # cursor.execute(final_sql)
            db_item = cursor.fetchall()
            arguments_string = " arg: %s" % str(args) if args else ''
            print("-----SQL: " + sql)
            if arguments_string:
                print("#####Params: " + arguments_string)
            return db_item
        except Exception as e:
            print("-----SQL数据库错误代码: {}, {}".format(e.args[0], e.args[1]))
            print("-----SQL: %s, 参数: %s", str(sql), str(args))
            print('-----SQL具体错误: ' + traceback.format_exc())
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @classmethod
    def insert_one(cls, table_name, args=None, connection_flag=ConnectionPool.ERP):
        try:
            import MySQLdb
            conn = None
            if connection_flag == ConnectionPool.ERP:
                conn = ksher_get_db_conn()
            if connection_flag == ConnectionPool.SETTLEMENT:
                conn = settlement_get_db_conn()

            cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

            fields_list = args.keys()
            fields_string = ','.join(fields_list)
            values_string = ','.join(["%({})s".format(e) for e in fields_list])

            sql = "INSERT INTO " + table_name + "(" + fields_string + ") VALUES(" + values_string + ") "

            arguments_string = " arg: %s" % str(args) if args else ''
            if arguments_string:
                print("#####Params: " + arguments_string)
            if args:
                row_count = cursor.execute(sql, args)
            else:
                row_count = cursor.execute(sql)
            conn.commit()
            print("-----SQL: " + sql + "; Result:" + str(row_count))
            return row_count
        except Exception as e:
            print("-----SQL数据库错误代码: {}, {}".format(e.args[0], e.args[1]))
            print("-----SQL: %s, 参数: %s", str(sql), str(args))
            print('-----SQL具体错误: ' + traceback.format_exc())
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @classmethod
    def delete(cls, table_name, args=None, connection_flag=ConnectionPool.ERP):
        try:
            import MySQLdb
            conn = ksher_get_db_conn()
            if connection_flag == ConnectionPool.ERP:
                conn = ksher_get_db_conn()
            if connection_flag == ConnectionPool.SETTLEMENT:
                conn = settlement_get_db_conn()
            cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)

            fields_list = args.keys()
            fields_string = ','.join(fields_list)
            values_string = ','.join(["%({})s".format(e) for e in fields_list])

            sql = "DELETE FROM " + table_name + "(" + fields_string + ") VALUES(" + values_string + ") "
            print("-----SQL: " + sql)
            arguments_string = " arg: %s" % str(args) if args else ''
            if arguments_string:
                print("#####Params: " + arguments_string)

            if args:
                row_count = cursor.execute(sql, args)
            else:
                row_count = cursor.execute(sql)
            conn.commit()
            return row_count
        except Exception as e:
            print("-----SQL数据库错误代码: {}, {}".format(e.args[0], e.args[1]))
            print("-----SQL: %s, 参数: %s", str(sql), str(args))
            print('-----SQL具体错误: ' + traceback.format_exc())
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @classmethod
    def update(cls, sql, args=None, connection_flag=ConnectionPool.ERP):
        try:
            import MySQLdb
            conn = None
            if connection_flag == ConnectionPool.ERP:
                conn = ksher_get_db_conn()
            if connection_flag == ConnectionPool.SETTLEMENT:
                conn = settlement_get_db_conn()

            cursor = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
            arguments_string = " arg: %s" % str(args) if args else ''
            print("-----SQL: " + sql)
            if arguments_string:
                print("#####Params: " + arguments_string)

            if args:
                row_count = cursor.execute(sql, args)
            else:
                row_count = cursor.execute(sql)
            conn.commit()
            return row_count
        except Exception as e:
            print("-----SQL数据库错误代码: {}, {}".format(e.args[0], e.args[1]))
            print("-----SQL: %s, 参数: %s", str(sql), str(args))
            print('-----SQL具体错误: ' + traceback.format_exc())
            if conn:
                conn.rollback()
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    @classmethod
    def insert(cls, sql, args, connection_flag=ConnectionPool.ERP):
        return cls.update(sql, args, connection_flag)

    @classmethod
    def delete(cls, sql, args, connection_flag=ConnectionPool.ERP):
        return cls.update(sql, args, connection_flag)

    @classmethod
    def get_select_sql(cls, table, fields, where_list=[]):
        sql = "SELECT " + fields + " FROM " + table
        if where_list:
            where_condition = ' AND '.join(where_list)
            sql += " WHERE " + where_condition
        return sql

    @classmethod
    def get_delete_sql(cls, table, where_list):
        where_condition = ' AND '.join(where_list)
        sql = "DELETE " + " FROM " + table + " WHERE " + where_condition
        return sql

    @classmethod
    def get_update_sql(cls, table, set_list, where_list):
        set_condition = ','.join([" {} = %({})s".format(e, e) for e in set_list])
        where_condition = ' AND '.join(where_list)
        sql = " UPDATE " + table + " SET " + set_condition + " WHERE " + where_condition
        return sql

    @classmethod
    def get_insert_sql_v1(cls, table, field_list):
        raw_field_str = ','.join(field_list)
        param_field_str = ','.join([" :{}".format(e) for e in field_list])
        sql = "INSERT INTO {} ({}) VALUES ({})".format(table, raw_field_str, param_field_str)
        return sql

    @classmethod
    def get_update_sql_v1(cls, table, set_list, where_list):
        set_condition = ','.join([" {} = :{}".format(e, e) for e in set_list])
        where_condition = ' AND '.join([" {} = :{}".format(e, e) for e in where_list])
        sql = " UPDATE " + table + " SET " + set_condition + " WHERE " + where_condition
        return sql


# d = {
#     '20181': {'mch_id': '20181', 'agency_id': 10077, 'agency_name': '', 'master_mch_id': '20175', 'master_mch_name': '',
#               'mch_name_local': '', 'mdr_agency_wechat': Decimal('0.60000'), 'mdr_agency_alipay': Decimal('1.00000'),
#               'transcation_count_wechat': 3, 'transcation_fee_wechat': -200, 'bank_psp_id': 15,
#               'transcation_count_alipay': 0, 'transcation_fee_alipay': 0, 'date': '2018-12-29',
#               'bank_fee_wechat': -0.0008999999999999999, 'bank_fee_alipay': 0.0},
#     '20182': {'mch_id': '20182', 'agency_id': 10077, 'agency_name': 'Japan-sakura01', 'master_mch_id': '20175',
#               'master_mch_name': '', 'mch_name_local': '', 'mdr_agency_wechat': Decimal('0.60000'),
#               'mdr_agency_alipay': Decimal('1.00000'), 'transcation_count_wechat': 18, 'transcation_fee_wechat': 0,
#               'bank_psp_id': 15, 'transcation_count_alipay': 0, 'transcation_fee_alipay': 0, 'date': '2018-12-29',
#               'bank_fee_wechat': 0.0, 'bank_fee_alipay': 0.0}}

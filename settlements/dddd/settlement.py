# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""

from settlements.sqlhelper import SQLHelper, ConnectionPool, settlement_get_db_conn, ksher_get_db_conn


class Report(object):
    ENDS_DATE = '2019-09-01'


    @classmethod
    def master_mch_count(cls, begin_date: str, end_date: str, bank_psp_id=15):
        sql = 'SELECT COUNT(*) FROM `mch_info` WHERE `is_master_mch`="Y" AND `bank_psp_id`="{bank_psp_id}" AND `create_time` BETWEEN "{begin_date}" AND "{end_date}" ORDER BY `create_time` DESC'.format(
            bank_psp_id=bank_psp_id, begin_date=begin_date, end_date=cls.ENDS_DATE)
        count = SQLHelper.select_one(sql)
        print(count.get('COUNT(*)'))
        return count.get('COUNT(*)')

    @classmethod
    def sub_mch_count(cls, begin_date, end_date, bank_psp_id=15):

        sql = 'SELECT COUNT(*) FROM `mch_info` WHERE `is_master_mch`="N" AND `bank_psp_id`="{bank_psp_id}" AND `create_time` BETWEEN "{begin_date}" AND "{end_date}" ORDER BY `create_time` DESC'.format(
            bank_psp_id=bank_psp_id, begin_date=begin_date, end_date=cls.ENDS_DATE)
        count = SQLHelper.select_one(sql)
        print(count.get('COUNT(*)'))
        return count.get('COUNT(*)')

    @classmethod
    def trading_wechat_count(cls, begin_date, end_date, bank_psp_id=15):
        sql = 'SELECT SUM(`pay_count`),SUM(`refund_count`),SUM(`revoked_count`) FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" AND `work_date` BETWEEN "{begin_date}" AND "{end_date}" AND `pay_channel`="{pay_channel}"'.format(
            bank_psp_id=bank_psp_id,
            begin_date=begin_date,
            end_date=end_date,
            pay_channel = 'wechat'
        )
        count = SQLHelper.select_one(sql,connection_flag=ConnectionPool.SETTLEMENT)
        pay_count = count.get('SUM(`pay_count`)') if count.get('SUM(`pay_count`)') else 0
        refund_count = count.get('SUM(`refund_count`)') if count.get('SUM(`refund_count`)') else 0
        revoked_count = count.get('SUM(`revoked_count`)') if count.get('SUM(`revoked_count`)') else 0
        count = pay_count + refund_count + refund_count
        return int(count)

    @classmethod
    def trading_alipay_count(cls, begin_date, end_date, bank_psp_id=15):
        sql = 'SELECT SUM(`pay_count`),SUM(`refund_count`),SUM(`revoked_count`) FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" AND `work_date` BETWEEN "{begin_date}" AND "{end_date}" AND `pay_channel`="{pay_channel}"'.format(
            bank_psp_id=bank_psp_id,
            begin_date=begin_date,
            end_date=end_date,
            pay_channel='alipay'
        )
        count = SQLHelper.select_one(sql, connection_flag=ConnectionPool.SETTLEMENT)
        pay_count = count.get('SUM(`pay_count`)') if count.get('SUM(`pay_count`)') else 0
        refund_count = count.get('SUM(`refund_count`)') if count.get('SUM(`refund_count`)') else 0
        revoked_count = count.get('SUM(`revoked_count`)') if count.get('SUM(`revoked_count`)') else 0
        count = pay_count  + refund_count + revoked_count
        return int(count)

    @classmethod
    def trading_alipay_wechat_count(cls, begin_date, end_date, bank_psp_id=15):
        return cls.trading_alipay_count(begin_date, end_date, bank_psp_id=bank_psp_id) + cls.trading_wechat_count(
            begin_date, end_date, bank_psp_id=bank_psp_id)

    @classmethod
    def trading_wechat_count_amount(cls, begin_date, end_date, bank_psp_id=15):
        sql = 'SELECT SUM(`transaction_fee`) FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" AND `work_date` BETWEEN "{begin_date}" AND "{end_date}" AND `pay_channel`="{pay_channel}"'.format(
            bank_psp_id=bank_psp_id,
            begin_date=begin_date,
            end_date=end_date,
            pay_channel='wechat'
        )
        count = SQLHelper.select_one(sql, connection_flag=ConnectionPool.SETTLEMENT)
        count = count.get('SUM(`transaction_fee`)')
        return int(count)

    @classmethod
    def trading_alipay_count_amount(cls, begin_date, end_date, bank_psp_id=15):
        sql = 'SELECT SUM(`transaction_fee`) FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" AND `work_date` BETWEEN "{begin_date}" AND "{end_date}" AND `pay_channel`="{pay_channel}"'.format(
            bank_psp_id=bank_psp_id,
            begin_date=begin_date,
            end_date=end_date,
            pay_channel='alipay'
        )
        count = SQLHelper.select_one(sql, connection_flag=ConnectionPool.SETTLEMENT)
        count = count.get('SUM(`transaction_fee`)')
        return int(count)

    @classmethod
    def trading_alipay_wechat_count_amount(cls, begin_date, end_date, bank_psp_id=15):
        return cls.trading_wechat_count_amount(begin_date, begin_date,
                                               bank_psp_id=bank_psp_id) + cls.trading_alipay_count_amount(begin_date,
                                                                                                          begin_date,
                                                                                                          bank_psp_id=bank_psp_id)

    @classmethod
    def insert_data(cls, begin_date, end_date=None, bank_psp_id=15):
        if not end_date:
            '''
            日报
            '''
            end_date = begin_date
        master_mch_count = cls.master_mch_count(begin_date, end_date)
        sub_mch_count = cls.sub_mch_count(begin_date, end_date)
        trading_wechat_count = cls.trading_wechat_count(begin_date, end_date)
        trading_alipay_count = cls.trading_alipay_count(begin_date, end_date)
        trading_alipay_wechat_count = cls.trading_alipay_wechat_count(begin_date, end_date)
        trading_wechat_count_amount = cls.trading_wechat_count_amount(begin_date, end_date)
        trading_alipay_count_amount = cls.trading_alipay_count_amount(begin_date, end_date)
        trading_alipay_wechat_count_amount = cls.trading_alipay_wechat_count_amount(begin_date, end_date)
        date = begin_date

        if end_date == begin_date:
            sql = 'SELECT * FROM `day_transaction_report` where `date`="{date}"'.format(date=date)
            counts = SQLHelper.select_one(sql=sql, connection_flag=ConnectionPool.SETTLEMENT)
            print(counts)
            if counts:
                pass
            else:
                sql = 'INSERT INTO `day_transaction_report`' \
                          ' (`master_mch_count`,' \
                          '`sub_mch_count`,' \
                          '`trading_wechat_count`,' \
                          '`trading_alipay_count`,' \
                          '`trading_alipay_wechat_count`,' \
                          '`trading_wechat_count_amount`,' \
                          '`trading_alipay_count_amount`,' \
                          '`trading_alipay_wechat_count_amount`,' \
                          '`date`) VALUES ("{master_mch_count}",' \
                          '"{sub_mch_count}",' \
                          '"{trading_wechat_count}",' \
                          '"{trading_alipay_count}",' \
                          '"{trading_alipay_wechat_count}",' \
                          '"{trading_wechat_count_amount}",' \
                          '"{trading_alipay_count_amount}",' \
                          '"{trading_alipay_wechat_count_amount}",' \
                          '"{date}")'.format(master_mch_count=master_mch_count, sub_mch_count=sub_mch_count,
                                             trading_wechat_count=trading_wechat_count,
                                             trading_alipay_count=trading_alipay_count,
                                             trading_alipay_wechat_count=trading_alipay_wechat_count,
                                             trading_wechat_count_amount=trading_wechat_count_amount,
                                             trading_alipay_count_amount=trading_alipay_count_amount,
                                             trading_alipay_wechat_count_amount=trading_alipay_wechat_count_amount,
                                             date=date)
                try:
                    row_count = SQLHelper.insert(sql=sql,args=None, connection_flag=ConnectionPool.SETTLEMENT)
                    '这儿写log'
                except Exception as e:
                    print(e)
                    '''
                    这儿写log
                    '''


        else:
            agency_sql = 'SELECT * FROM `week_transaction_report` where `begin_time`="{begin_time}" and end_time="{end_time}"'.format(begin_time=begin_date,end_time=end_date)
            row_count = SQLHelper.select_all(agency_sql,connection_flag=ConnectionPool.SETTLEMENT)
            print(row_count)
            if not row_count:
                pass
            else:
                '''
                每个对应的要插入4条渠道数据分别计算渠道收益
                '''




if __name__ == '__main__':
    # Report.insert_data(begin_date="2018-12-29")
    Report.insert_data(begin_date="2018-12-29", end_date="2019-01-21")

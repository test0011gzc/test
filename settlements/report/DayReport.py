other_config = {
    '10215': {'wechat': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr': 'Y'},
              'alipay': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45}
              },
    '20368': {'wechat': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45},
              'alipay': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45}
              },
    '20367': {'wechat': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45},
              'alipay': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45}
              },
    '0': 'xx'
}
from settlements.sqlhelper import SQLHelper, ConnectionPool
import datetime

class DayReport(object):
    BEGIN_DATE = '2019-09-01'
    mch_info_item = None
    payment_transaction_sum_item = None
    mch_dict = {}
    @property
    def mch_info(self, bank_psp_id=15):
        if self.mch_info_item:
            return self.mch_info_item
        mch_info_sql = 'SELECT * FROM `mch_info` WHERE `bank_psp_id`="{}" and account_type="Formal"'.format(bank_psp_id)
        mch_info_dict = SQLHelper.select_all(sql=mch_info_sql)
        print('#' * 10 + 'mch_info_dict')
        print(mch_info_dict)
        self.mch_info_item = mch_info_dict
        return self.mch_info_item

    @property
    def mch_info_to_dict(self):
        if self.mch_dict:
            return self.mch_dict
        else:
            mch_infos = self.mch_info
            for mch_info in mch_infos:
                self.mch_dict[mch_info['mch_id']] = mch_info
            return self.mch_dict


    @property
    def payment_transaction_sum(self, bank_psp_id=15):
        if self.payment_transaction_sum_item:
            return self.payment_transaction_sum_item
        payment_transaction_sum_sql = 'SELECT * FROM `payment_transaction_sum` WHERE `bank_psp_id`="{}"'.format(
            bank_psp_id)
        payment_transaction_sum_dict = SQLHelper.select_all(sql=payment_transaction_sum_sql,
                                                            connection_flag=ConnectionPool.SETTLEMENT)
        self.payment_transaction_sum_item = payment_transaction_sum_dict
        return self.payment_transaction_sum_item

    def master_mch_count(self, end_date: str):
        if end_date < self.BEGIN_DATE:
            raise Exception('结束时间不能小于2019-09-01')
        mch_info_dict = self.mch_info
        count = len([mch_info for mch_info in mch_info_dict if
                     mch_info.get('is_master_mch') == 'Y' and mch_info.get('create_time').strftime(
                         '%Y-%m-%d') <= end_date])
        return int(count)
    def get_channel(self,channel,end_date):
        master_mch_id = [mch_info['mch_id'] for mch_info in self.mch_info if mch_info.get('is_master_mch') == 'Y' and mch_info.get('create_time').strftime(
                         '%Y-%m-%d') <= end_date]
        use_channel = 'N'
        mch_fee_rate_flow_sql =  'SELECT * FROM `mch_fee_rate_flow` where channel_id="{}"'.format(channel)
        mch_fee_rate_flow_dict = SQLHelper.select_all(sql=mch_fee_rate_flow_sql)
        mch_fee_rate_flow_dict = {mch['mch_id']:mch for mch in mch_fee_rate_flow_dict}
        for mch_id in master_mch_id:
            mch_fee_rate_flow = mch_fee_rate_flow_dict.get(mch_id)
            if mch_fee_rate_flow:
                if mch_fee_rate_flow['begin_date'] <= datetime.datetime.strptime(end_date,'%Y-%m-%d').strftime('%Y-%m-%d %H:%M:%S') <= mch_fee_rate_flow['end_date']:
                        use_channel = 'Y'
                        return use_channel
                else:
                    continue
            else:
                continue
        return use_channel
    def sub_mch_count(self, end_date: str):
        if end_date < self.BEGIN_DATE:
            raise Exception('结束时间不能小于2019-09-01')
        mch_info_dict = self.mch_info
        count = len([mch_info for mch_info in mch_info_dict if
                     mch_info.get('is_master_mch') == 'N' and  mch_info.get(
                         'create_time').strftime('%Y-%m-%d') <= end_date])
        return int(count)

    def transcation_count(self, begin_date, end_date, channel):
        payment_transaction_sum = self.payment_transaction_sum
        pay_count_sum_list = []
        refund_count_list = []
        revoked_count_list = []
        for payment_transaction in payment_transaction_sum:
            if payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction['work_date'] <= end_date:
                try:
                    mch_info_obj = self.mch_info_to_dict.get(payment_transaction['mch_id'])
                    if mch_info_obj.get('account_type') == "Formal":
                        pay_count_sum_list.append(payment_transaction['pay_count'])
                        refund_count_list.append(payment_transaction['refund_count'])
                        revoked_count_list.append(payment_transaction['revoked_count'])
                except AttributeError:
                    print('%s是测试商户' % payment_transaction['mch_id'])
                    continue
        # pay_count_sum = sum(
        #     [payment_transaction['pay_count'] if payment_transaction['pay_count'] else 0 for payment_transaction in
        #      payment_transaction_sum if
        #      payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction[
        #          'work_date'] <= end_date])
        # refund_count = sum(
        #     [payment_transaction['refund_count'] if payment_transaction['refund_count'] else 0 for payment_transaction
        #      in payment_transaction_sum if
        #      payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction[
        #          'work_date'] <= end_date])
        # revoked_count = sum(
        #     [payment_transaction['revoked_count'] if payment_transaction['revoked_count'] else 0 for payment_transaction
        #      in payment_transaction_sum if
        #      payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction[
        #          'work_date'] <= end_date])

        return sum(pay_count_sum_list) + sum(refund_count_list) + sum(revoked_count_list)

    def trading_count_amount(self, begin_date, end_date, channel):
        payment_transaction_sum = self.payment_transaction_sum
        list_ = []
        for payment_transaction in payment_transaction_sum:
            if payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction['work_date'] <= end_date:
                try:
                    mch_info_obj = self.mch_info_to_dict.get(payment_transaction['mch_id'])
                    if mch_info_obj.get('account_type') == "Formal":
                        list_.append(payment_transaction['transaction_fee'])
                except AttributeError:
                    print('%s是测试商户'%payment_transaction['mch_id'])
                    continue
        print(list_)
        channel_sum = sum(list_)
        return channel_sum

    def insert_data(self,date,bank_psp_id=15):
        select_sql = 'select * from day_transaction_report where transaction_date="{}" '.format(date)
        row_count = SQLHelper.insert(sql=select_sql, args=None, connection_flag=ConnectionPool.SETTLEMENT)
        if row_count:
            pass
        else:
            sql = 'INSERT INTO `day_transaction_report`' \
                  ' (`transaction_date`,' \
                   ' `master_mch_count`, ' \
                  '`bank_psp_id`,' \
                  '`sub_mch_count`,' \
                  '`transaction_count_wechat`,' \
                  '`transaction_count_alipay`,' \
                  '`transaction_fee_alipay`,' \
                  '`transaction_fee_wechat`,' \
                  '`use_wechat`,' \
                  '`use_alipay`) VALUES ("{transaction_date}",' \
                  '"{master_mch_count}",' \
                  '"{bank_psp_id}",' \
                  '"{sub_mch_count}",' \
                  '"{transaction_count_wechat}",' \
                  '"{transaction_count_alipay}",' \
                  '"{transaction_fee_alipay}",' \
                  '"{transaction_fee_wechat}",' \
                  '"{use_wechat}",' \
                  '"{use_alipay}")'.format(bank_psp_id=bank_psp_id,sub_mch_count=self.sub_mch_count(end_date=date),
                                                       transaction_count_wechat=self.transcation_count(begin_date=date,end_date=date,channel="wechat"),
                                                       transaction_count_alipay=self.transcation_count(begin_date=date,end_date=date,channel="alipay"),
                                                       transaction_fee_wechat=self.trading_count_amount(begin_date=date,end_date=date,channel='wechat'),
                                                       transaction_fee_alipay=self.trading_count_amount(begin_date=date,
                                                                                                        end_date=date,
                                                                                                        channel='alipay'),
                                                       transaction_date=date,master_mch_count=self.master_mch_count(end_date=date),
                                                        use_wechat = self.get_channel('wechat',date),
                                                        use_alipay =  self.get_channel('alipay',date),
                                                       )
            try:
                row_count = SQLHelper.insert(sql=sql, args=None, connection_flag=ConnectionPool.SETTLEMENT)
                print(row_count)
            except Exception as e:
                print(e)


#
if __name__ == '__main__':
    DayReport().insert_data(date="2019-09-02")
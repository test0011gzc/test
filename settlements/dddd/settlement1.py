
from settlements.sqlhelper import SQLHelper, ConnectionPool, settlement_get_db_conn, ksher_get_db_conn

conf = {
    'LE_TIAN_BANK': 15,
    'LE_TIAN_PAY': 16,
    'KSHER': 17,
    'SN': 18,
    'OTHER': 19,
}

other_config = {
    '10215': {'wechat': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45},
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



#
# trans_list =
# [
#     {'mch_id': 11, 'agency_id': 'xx'}
# ]
#
# for e in other_config:
#     result = []
#     all_total_fee = 0
#     if e.key != 0:
#         all_total_fee = sum(x['transactioN_fee'] for x in trans_list if x['agency_id'] == e)
#         item = {}
#         result.append(item)
#
#         # sum->db
#
#     else:
#         # 吧key 不在other_config中的更为为0
#         # sum-》db
#
#     final_result = {'list_part': result, 'summary_par': 'xx'}

###############
# [
#     {
#         'begin_date': '2019-09-01',
#         'end_date': '2019-09-15',
#         'agency_id': 1034,
#         'agency_name': 'Rakuten',
#         'master_mch_id': '20195',
#         'master_mch_name': 'MasterName',
#         'sub_mch_count': 2,
#         'mdr': {
#             'wechat': 1.7,
#             'alipay': 2.5
#         },
#         'transaction_count': {
#             'wechat': 1,
#             'alipay': 3
#         },
#         'transaction_fee': {
#             'wechat': 400,
#             'alipay': 270
#         },
#         'agency_profit': {
#             'wechat': 12,
#             'alipay': 5
#         }
#     }
# ]

stub_data = {
    'total_count': 19,
    'begin_date': '2019-09-01',
    'end_date': '2019-09-15',
    'data': [
        {
            'agency_id': 102, 'agency_name': 'rRautken', 'count': 3,
            'master_mch_id': '20195',
            'master_mch_name': '付商户名',

            'data_list': [{

                'sub_mch_name': '子商户名',
                'sub_mch_count': 2,  # 店铺数
                'mdr': {
                    'wechat': 1.7,
                    'alipay': ''
                },
                'transaction_count': {
                    'wechat': 1,
                    'alipay': 0,
                    'wechat+alipay': 0
                },
                'transaction_fee': {
                    'wechat': 400,
                    'alipay': 270,
                    'wechat+alipay': 0
                },
                'agency_profit': {
                    'wechat': 12,
                    'alipay': 5,
                    'wechat+alipay': 0
                }
            }, {
                'master_mch_id': '20195',
                'master_mch_name': 'MasterName',
                'sub_mch_count': 2,
                'mdr': {
                    'wechat': 1.7,
                    'alipay': 2.5
                },
                'transaction_count': {
                    'wechat': 1,
                    'alipay': 3
                },
                'transaction_fee': {
                    'wechat': 400,
                    'alipay': 270
                },
                'agency_profit': {
                    'wechat': 12,
                    'alipay': 5
                }
            }, {

                'master_mch_id': '20195',
                'master_mch_name': 'MasterName',
                'sub_mch_count': 2,
                'mdr': {
                    'wechat': 1.7,
                    'alipay': 2.5
                },
                'transaction_count': {
                    'wechat': 1,
                    'alipay': 3
                },
                'transaction_fee': {
                    'wechat': 400,
                    'alipay': 270
                },
                'agency_profit': {
                    'wechat': 12,
                    'alipay': 5
                }
            }]
        },

    ]
}
day_data = [
    {
        'date': '',
        'master_mch_count': 70,
        'sub_mch_count': 700,
        'mdr': {
            'wechat': 1.7,
            'alipay': 2.5
        },
        'transaction_count': {
            'wechat': 1,
            'alipay': 3
        },
        'transaction_fee': {
            'wechat': 400,
            'alipay': 270
        },
    },
]


###############


class Report(object):
    BEGIN_DATE = '2019-09-01'
    payment_transaction_sum_item = None
    mch_info_item = None
    mch_fee_rate_flow_item = None
    agency_item = None
    db_item = {}
    agency_data = None
    week_transaction = None

    def weektransaction(self,begin_date,end_date):
        sql = 'select mch_id,begin_date,end_date from week_transaction where  '

    @property
    def agencydata(self):
        if self.agency_data:
            return self.agency_data
        self.agency_data = {agency['id']:agency for agency in self.agency}
        return self.agency_data

    # @property
    # def db_data(self):
    #     if self.db_item:
    #         return self.db_item
    #     db_item = {payment['mch_id'] + '_' +payment['channel'] : payment for payment in self.payment_transaction_sum}
    #     mch_info_dict = {}
    #     for mch_info in self.mch_info:
    #         mch_info['mch_info_id'] = mch_info['id']
    #         mch_info_dict.update({mch_info['mch_id']: mch_info})
    #     for item in db_item:
    #         mch_id = item.split('_')[0]
    #         db_item[mch_id+'_'+'wechat'].update(mch_info_dict[mch_id])
    #         db_item[mch_id + '_' + 'alipay'].update(mch_info_dict[mch_id])
    #     self.db_item = db_item
    #     return self.db_item

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

    @property
    def mch_info(self, bank_psp_id=15):
        if self.mch_info_item:
            return self.mch_info_item
        mch_info_sql = 'SELECT * FROM `mch_info` WHERE `bank_psp_id`="{}"'.format(bank_psp_id)
        mch_info_dict = SQLHelper.select_all(sql=mch_info_sql)
        print('#' * 10 + 'mch_info_dict')
        print(mch_info_dict)
        self.mch_info_item = mch_info_dict
        return self.mch_info_item

    @property
    def mch_fee_rate_flow(self):
        if self.mch_fee_rate_flow_item:
            return self.mch_fee_rate_flow_item
        mch_fee_rate_flow_sql = 'SELECT * FROM `mch_fee_rate_flow`'
        mch_fee_rate_flow_dict = SQLHelper.select_all(sql=mch_fee_rate_flow_sql)
        self.mch_fee_rate_flow_item = mch_fee_rate_flow_dict
        return self.mch_fee_rate_flow_item

    @property
    def agency(self, bank_psp_id=15):
        if self.agency_item:
            return self.agency_item
        agency_sql = 'SELECT * FROM `agencies` WHERE `bank_psp_id`="{}"'.format(bank_psp_id)
        agency_dict = SQLHelper.select_all(sql=agency_sql)
        self.agency_item = agency_dict
        return self.agency_item

    def master_mch_count(self, end_date: str):
        if end_date < self.BEGIN_DATE:
            raise Exception('结束时间不能小于2019-09-01')
        mch_info_dict = self.mch_info
        count = len([mch_info for mch_info in mch_info_dict if
                     mch_info.get('is_master_mch') == 'Y' and self.BEGIN_DATE <= mch_info.get('create_time').strftime(
                         '%Y-%m-%d') <= end_date])
        return count

    def sub_mch_count(self, end_date: str):
        if end_date < self.BEGIN_DATE:
            raise Exception('结束时间不能小于2019-09-01')
        mch_info_dict = self.mch_info
        count = len([mch_info for mch_info in mch_info_dict if
                     mch_info.get('is_master_mch') == 'N' and self.BEGIN_DATE <= mch_info.get(
                         'create_time') <= end_date])
        return count

    def trading_count(self, begin_date, end_date, channel):
        payment_transaction_sum = self.payment_transaction_sum
        pay_count_sum = sum(
            [payment_transaction['pay_count'] if payment_transaction['pay_count'] else 0 for payment_transaction in
             payment_transaction_sum if
             payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction[
                 'work_date'] <= end_date])
        refund_count = sum(
            [payment_transaction['refund_count'] if payment_transaction['refund_count'] else 0 for payment_transaction
             in payment_transaction_sum if
             payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction[
                 'work_date'] <= end_date])
        revoked_count = sum(
            [payment_transaction['revoked_count'] if payment_transaction['revoked_count'] else 0 for payment_transaction
             in payment_transaction_sum if
             payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction[
                 'work_date'] <= end_date])
        return pay_count_sum + refund_count + revoked_count

    def trading_count_amount(self, begin_date, end_date, channel):
        payment_transaction_sum = self.payment_transaction_sum
        channel_sum = sum([payment_transaction['transaction_fee'] if payment_transaction['transaction_fee'] else 0 for
                           payment_transaction in payment_transaction_sum if
                           payment_transaction['pay_channel'] == channel and begin_date <= payment_transaction[
                               'work_date'] <= end_date])
        return channel_sum

    def clac_agency_earnings(self, begin_date, end_date, channel):
        mch_bank_fees = {}
        for key,val in self.db_data.items():
            if val['pay_channel'] == channel  and begin_date <= val['work_date'] <= end_date and val['is_master_mch'] == 'N':
                parmas = other_config.get(str(val['agency_id']))
                if not parmas:
                    #说明是其他渠道 #计算当前商户的银行收益
                    mch_bank_fee = (val['transaction_fee']/100) * (((other_config['0'][channel]['mdr_agency'] - other_config['0'][channel]['mdr_cost']) / 100) * other_config['0'][channel]['factor'])
                else:
                    #判断这个渠道是不是乐天银行的渠道、  没有channel
                    mdr_agency = parmas.get(channel).get('mdr_agency')
                    if not mdr_agency:
                        # 这里表示是乐天银行渠道 需要从里一个数据中获取
                        #当前商户对应channel的费率为
                        try:
                            mdr_agency = [mch_fee_rate['ksher_fee_rate']  for mch_fee_rate in self.mch_fee_rate_flow if mch_fee_rate['mch_id'] == val['mch_id'] and mch_fee_rate['channel_id'] == channel][0]
                        except Exception as e:
                            mdr_agency = 0

                        mch_bank_fee = (val['transaction_fee'] / 100) * (((mdr_agency -
                                                                           parmas[channel][
                                                                               'mdr_cost']) / 100) *
                                                                         parmas[channel]['factor'])


                    else:
                        #这里表示的是除了乐天银行和其他渠道之外的渠道
                        mch_bank_fee = (val['transaction_fee'] / 100) * (((parmas[channel]['mdr_agency'] -
                                                                           parmas[channel][
                                                                               'mdr_cost']) / 100) *
                                                                         parmas[channel]['factor'])
                mch_bank_fees['mch_id'] = mch_bank_fee
        return mch_bank_fees

        # for keys in other_config:
        #     if keys != 0:
        #         mch_bank_fee_dict = {key: val['transaction_fee'] / 100 * (((other_config[keys][channel]['mdr_agency'] -
        #                                                                     other_config[keys][channel][
        #                                                                         'mdr_cost']) / 100) *
        #                                                                   other_config[keys][channel]['factor'])
        #                              for key, val in self.db_data.items() if
        #                              val['pay_channel'] == channel and val['agency_id'] == keys and begin_date <= val[
        #                                  'work_date'] <= end_date and val['is_master_mch'] == 'N'}

        pass
        # channel_payment_transaction_list = [payment_transaction for payment_transaction in self.payment_transaction_sum
        #                                     if payment_transaction['pay_channel'] == channel and begin_date <=
        #                                     payment_transaction['work_date'] <= end_date]
        # if channel == 'wechat':
        #     mdr_agency = 0.5 / 100
        # else:
        #     mdr_agency = 0.8 / 100
        # factor = 0.45
        # channel_count_amout = 0
        # for channel_payment_transaction in channel_payment_transaction_list:
        #
        #     ksher_fee_rate = self.mch_fee_rate_flow_d.get(channel_payment_transaction['mch_id']).get(
        #         'ksher_fee_rate')  # 获取当前商户的费率
        #     agency_id = self.mch_info_d.get(channel_payment_transaction['mch_id']).get('agency_id')  # 当前商户的渠道
        #     if agency_id == conf.get('LE_TIAN_BANK'):  # 假设15 乐天银行   16 乐天pay  17 kesher 18  sn山口组  19 其他
        #         # 当前商户的收益
        #         amount = channel_payment_transaction['channel_payment_transaction'] * (
        #                 (ksher_fee_rate / 100 - a) * 0.45)
        #         channel_count_amout += amount
        #     if agency_id == conf.get('LE_TIAN_PAY'):
        #         amount = channel_payment_transaction['channel_payment_transaction'] * ((1.7 / 100 - a) * 0.45)
        #         channel_count_amout += amount
        #     if agency_id == conf.get('KSHER'):
        #         if channel == 'wechat':
        #             mdr_cost = 1.7 / 100
        #         else:
        #             mdr_cost = 1.8 / 100
        #         amount = channel_payment_transaction['channel_payment_transaction'] * ((b - a) * 0.45)
        #         channel_count_amout += amount
        #     if agency_id == conf.get('SN'):
        #
        #         mdr_agency
        #         mdr_cost
        #         factor
        #
        #         if channel == 'wechat':
        #             b = 1.65 / 100
        #         else:
        #             b = 1.8 / 100
        #         amount = channel_payment_transaction['channel_payment_transaction'] * ((b - a) * 0.45)
        #         channel_count_amout += amount
        #     if agency_id == 19:
        #         amount = channel_payment_transaction['channel_payment_transaction'] * ((1.8 / 100 - a) * 0.45)
        #         channel_count_amout += amount
        # return channel_count_amout

    def insert_day_transaction_report(self, date):
        master_mch_count = self.master_mch_count(date)
        sub_mch_count = self.sub_mch_count(date)
        trading_wechat_count = self.trading_count(date, date, 'wechat')
        trading_alipay_count = self.trading_count(date, date, 'alipay')
        trading_alipay_wechat_count = trading_wechat_count + trading_alipay_count
        trading_wechat_count_amount = self.trading_count_amount(date, date, "wechat")
        trading_alipay_count_amount = self.trading_count_amount(date, date, "alipay")
        trading_alipay_wechat_count_amount = trading_wechat_count_amount + trading_alipay_count_amount
        sql = 'SELECT * FROM `day_transaction_report` where `date`="{date}"'.format(date=date)
        counts = SQLHelper.select_one(sql, connection_flag=ConnectionPool.SETTLEMENT)
        if counts:
            return
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
                row_count = SQLHelper.insert(sql=sql, args=None, connection_flag=ConnectionPool.SETTLEMENT)
                '这儿写log'
            except Exception as e:
                print(e)
                '''
                这儿写log
                '''

    def insert_week_transaction_report(self, begin_date,end_date):
        for key,val in self.db_data:
            if begin_date <= val['work_date'] <= end_date and val['is_master_mch'] == 'N':
                master_mdr_dict = {mch_fee_rate['channel_id']:mch_fee_rate['ksher_fee_rate']  for mch_fee_rate in self.mch_fee_rate_flow if mch_fee_rate['mch_id'] == val['mch_id']}
                data = {
                    'agency_id':val['agency_id'],
                    'agency_name':self.agencydata.get(val['agency_id']),
                    'master_name':self.db_data.get(val['master_mch_id'])['mch_name_local'],
                    'mch_id':val['mch_id'],
                    'master_mdr_wechat': master_mdr_dict.get('wechat',0),
                    'master_mdr_alipay': master_mdr_dict.get('alipay',0),
                    'transaction_count_wechat':self.db_data.get(key.split('_')[0] + 'wechat')['pay_count'] + self.db_data.get(key.split('_')[0] + 'wechat')['refund_count'] +self.db_data.get(key.split('_')[0] + 'wechat')['revoked_count']
                    'transaction_count_alipay': self.db_data.get(key.split('_')[0] + 'alipay')['pay_count'] +
                                                self.db_data.get(key.split('_')[0] + 'alipay')['refund_count'] +
                                                self.db_data.get(key.split('_')[0] + 'alipay')['revoked_count'],
                    'bank_fee_wechat':self.clac_agency_earnings(begin_date,end_date,'wechat'),
                    'bank_fee_alipay':self.clac_agency_earnings(begin_date,end_date,'alipay')
                }





#     @classmethod
#     def master_mch_count(cls, begin_date: str, end_date: str, bank_psp_id=15):
#         sql = 'SELECT COUNT(*) FROM `mch_info` WHERE `is_master_mch`="Y" AND `bank_psp_id`="{bank_psp_id}" AND `create_time` BETWEEN "{begin_date}" AND "{end_date}" ORDER BY `create_time` DESC'.format(
#             bank_psp_id=bank_psp_id, begin_date=begin_date, end_date=cls.ENDS_DATE)
#         count = SQLHelper.select_one(sql)
#         print(count.get('COUNT(*)'))
#         return count.get('COUNT(*)')
#
#     @classmethod
#     def sub_mch_count(cls, begin_date, end_date, bank_psp_id=15):
#
#         sql = 'SELECT COUNT(*) FROM `mch_info` WHERE `is_master_mch`="N" AND `bank_psp_id`="{bank_psp_id}" AND `create_time` BETWEEN "{begin_date}" AND "{end_date}" ORDER BY `create_time` DESC'.format(
#             bank_psp_id=bank_psp_id, begin_date=begin_date, end_date=cls.ENDS_DATE)
#         count = SQLHelper.select_one(sql)
#         print(count.get('COUNT(*)'))
#         return count.get('COUNT(*)')
#
#     @classmethod
#     def trading_wechat_count(cls, begin_date, end_date, bank_psp_id=15):
#         sql = 'SELECT SUM(`pay_count`),SUM(`refund_count`),SUM(`revoked_count`) FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" AND `work_date` BETWEEN "{begin_date}" AND "{end_date}" AND `pay_channel`="{pay_channel}"'.format(
#             bank_psp_id=bank_psp_id,
#             begin_date=begin_date,
#             end_date=end_date,
#             pay_channel='wechat'
#         )
#         count = SQLHelper.select_one(sql, connection_flag=ConnectionPool.SETTLEMENT)
#         pay_count = count.get('SUM(`pay_count`)') if count.get('SUM(`pay_count`)') else 0
#         refund_count = count.get('SUM(`refund_count`)') if count.get('SUM(`refund_count`)') else 0
#         revoked_count = count.get('SUM(`revoked_count`)') if count.get('SUM(`revoked_count`)') else 0
#         count = pay_count + refund_count + refund_count
#         return int(count)
#
#     @classmethod
#     def trading_alipay_count(cls, begin_date, end_date, bank_psp_id=15):
#         sql = 'SELECT SUM(`pay_count`),SUM(`refund_count`),SUM(`revoked_count`) FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" AND `work_date` BETWEEN "{begin_date}" AND "{end_date}" AND `pay_channel`="{pay_channel}"'.format(
#             bank_psp_id=bank_psp_id,
#             begin_date=begin_date,
#             end_date=end_date,
#             pay_channel='alipay'
#         )
#         count = SQLHelper.select_one(sql, connection_flag=ConnectionPool.SETTLEMENT)
#         pay_count = count.get('SUM(`pay_count`)') if count.get('SUM(`pay_count`)') else 0
#         refund_count = count.get('SUM(`refund_count`)') if count.get('SUM(`refund_count`)') else 0
#         revoked_count = count.get('SUM(`revoked_count`)') if count.get('SUM(`revoked_count`)') else 0
#         count = pay_count + refund_count + revoked_count
#         return int(count)
#
#     @classmethod
#     def trading_alipay_wechat_count(cls, begin_date, end_date, bank_psp_id=15):
#         return cls.trading_alipay_count(begin_date, end_date, bank_psp_id=bank_psp_id) + cls.trading_wechat_count(
#             begin_date, end_date, bank_psp_id=bank_psp_id)
#
#     @classmethod
#     def trading_wechat_count_amount(cls, begin_date, end_date, bank_psp_id=15):
#         sql = 'SELECT SUM(`transaction_fee`) FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" AND `work_date` BETWEEN "{begin_date}" AND "{end_date}" AND `pay_channel`="{pay_channel}"'.format(
#             bank_psp_id=bank_psp_id,
#             begin_date=begin_date,
#             end_date=end_date,
#             pay_channel='wechat'
#         )
#         count = SQLHelper.select_one(sql, connection_flag=ConnectionPool.SETTLEMENT)
#         count = count.get('SUM(`transaction_fee`)')
#         return int(count)
#
#     @classmethod
#     def trading_alipay_count_amount(cls, begin_date, end_date, bank_psp_id=15):
#         sql = 'SELECT SUM(`transaction_fee`) FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" AND `work_date` BETWEEN "{begin_date}" AND "{end_date}" AND `pay_channel`="{pay_channel}"'.format(
#             bank_psp_id=bank_psp_id,
#             begin_date=begin_date,
#             end_date=end_date,
#             pay_channel='alipay'
#         )
#         count = SQLHelper.select_one(sql, connection_flag=ConnectionPool.SETTLEMENT)
#         count = count.get('SUM(`transaction_fee`)')
#         return int(count)
#
#     @classmethod
#     def trading_alipay_wechat_count_amount(cls, begin_date, end_date, bank_psp_id=15):
#         return cls.trading_wechat_count_amount(begin_date, begin_date,
#                                                bank_psp_id=bank_psp_id) + cls.trading_alipay_count_amount(begin_date,
#                                                                                                           begin_date,
#                                                                                                           bank_psp_id=bank_psp_id)
#
#     @classmethod
#     def insert_data(cls, begin_date, end_date=None, bank_psp_id=15):
#         if not end_date:
#             '''
#             日报
#             '''
#             end_date = begin_date
#         master_mch_count = cls.master_mch_count(begin_date, end_date)
#         sub_mch_count = cls.sub_mch_count(begin_date, end_date)
#         trading_wechat_count = cls.trading_wechat_count(begin_date, end_date)
#         trading_alipay_count = cls.trading_alipay_count(begin_date, end_date)
#         trading_alipay_wechat_count = cls.trading_alipay_wechat_count(begin_date, end_date)
#         trading_wechat_count_amount = cls.trading_wechat_count_amount(begin_date, end_date)
#         trading_alipay_count_amount = cls.trading_alipay_count_amount(begin_date, end_date)
#         trading_alipay_wechat_count_amount = cls.trading_alipay_wechat_count_amount(begin_date, end_date)
#         date = begin_date
#
#         if end_date == begin_date:
#             sql = 'SELECT * FROM `day_transaction_report` where `date`="{date}"'.format(date=date)
#             counts = SQLHelper.select_one(sql=sql, connection_flag=ConnectionPool.SETTLEMENT)
#             print(counts)
#             if counts:
#                 pass
#             else:
#                 sql = 'INSERT INTO `day_transaction_report`' \
#                       ' (`master_mch_count`,' \
#                       '`sub_mch_count`,' \
#                       '`trading_wechat_count`,' \
#                       '`trading_alipay_count`,' \
#                       '`trading_alipay_wechat_count`,' \
#                       '`trading_wechat_count_amount`,' \
#                       '`trading_alipay_count_amount`,' \
#                       '`trading_alipay_wechat_count_amount`,' \
#                       '`date`) VALUES ("{master_mch_count}",' \
#                       '"{sub_mch_count}",' \
#                       '"{trading_wechat_count}",' \
#                       '"{trading_alipay_count}",' \
#                       '"{trading_alipay_wechat_count}",' \
#                       '"{trading_wechat_count_amount}",' \
#                       '"{trading_alipay_count_amount}",' \
#                       '"{trading_alipay_wechat_count_amount}",' \
#                       '"{date}")'.format(master_mch_count=master_mch_count, sub_mch_count=sub_mch_count,
#                                          trading_wechat_count=trading_wechat_count,
#                                          trading_alipay_count=trading_alipay_count,
#                                          trading_alipay_wechat_count=trading_alipay_wechat_count,
#                                          trading_wechat_count_amount=trading_wechat_count_amount,
#                                          trading_alipay_count_amount=trading_alipay_count_amount,
#                                          trading_alipay_wechat_count_amount=trading_alipay_wechat_count_amount,
#                                          date=date)
#                 try:
#                     row_count = SQLHelper.insert(sql=sql, args=None, connection_flag=ConnectionPool.SETTLEMENT)
#                     '这儿写log'
#                 except Exception as e:
#                     print(e)
#                     '''
#                     这儿写log
#                     '''
#
#
#         else:
#             agency_sql = 'SELECT * FROM `week_transaction_report` where `begin_time`="{begin_time}" and end_time="{end_time}"'.format(
#                 begin_time=begin_date, end_time=end_date)
#             row_count = SQLHelper.select_all(agency_sql, connection_flag=ConnectionPool.SETTLEMENT)
#             print(row_count)
#             if not row_count:
#                 pass
#             else:
#                 '''
#                 每个对应的要插入4条渠道数据分别计算渠道收益
#                 '''
#
#
if __name__ == '__main__':
    # report = Report()
    # print(report.master_mch_count('2019-12-29'))
    # #     Report.insert_data(begin_date="2018-12-29", end_date="2019-01-21")
    # print(report.db_data)

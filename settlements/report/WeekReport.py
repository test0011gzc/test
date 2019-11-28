# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""
other_config = {
    '10204': {'wechat': {'mdr_agency': 1.7, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr_wechat': 'Y'},
              'alipay': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45,'use_master_mdr_alipay': 'Y'}
              },
    '10186': {'wechat': {'mdr_agency': 1.7, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr_wechat': 'N'},
              'alipay': {'mdr_agency': 1.7, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr_alipay': 'N'}
              },
    '10209': {'wechat': {'mdr_agency': 1.65, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr_wechat': 'N'},
              'alipay': {'mdr_agency': 1.8, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr_alipay': 'N'}
              },
    '10203': {'wechat': {'mdr_agency': 1.65, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr_wechat': 'N'},
              'alipay': {'mdr_agency': 1.8, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr_alipay': 'N'}
              },
    '0':     {'wechat': {'mdr_agency': 1.8, 'mdr_cost': 0.5, 'factor': 0.45, 'use_master_mdr_wechat': 'N'},
              'alipay': {'mdr_agency': 1.8, 'mdr_cost': 0.8, 'factor': 0.45, 'use_master_mdr_alipay': 'N'}
              },
}

from settlements.sqlhelper import SQLHelper, ConnectionPool


class WeekReport(object):
    payment_transaction_sum_item = None
    new_dict = {}
    mch_info_dict = {}
    agency_dict = {}
    mch_fee_rate_flow_item = None
    BEGIN_DATE = '2019-09-01'

    @property
    def mch_fee_rate_flow(self):
        if self.mch_fee_rate_flow_item:
            return self.mch_fee_rate_flow_item
        mch_fee_rate_flow_sql = 'SELECT * FROM `mch_fee_rate_flow`'
        mch_fee_rate_flow_dict = SQLHelper.select_all(sql=mch_fee_rate_flow_sql)
        self.mch_fee_rate_flow_item = mch_fee_rate_flow_dict
        return self.mch_fee_rate_flow_item

    @property
    def get_agencies(self):
        if self.agency_dict:
            return self.agency_dict
        agency_sql = 'SELECT * FROM `agencies`'
        self.agency_dict = {agency['id']: agency for agency in SQLHelper.select_all(sql=agency_sql)}
        return self.agency_dict

    @property
    def get_mch_infos(self, bank_psp_id=15):
        if self.mch_info_dict:
            return self.mch_info_dict
        mch_info_sql = 'SELECT * FROM `mch_info` WHERE `bank_psp_id`="{}" and account_type="Formal"'.format(bank_psp_id)
        self.mch_info_dict = {mch['mch_id']: mch for mch in SQLHelper.select_all(sql=mch_info_sql)}
        return self.mch_info_dict

    def payment_transaction_sum(self, begin_date, end_date, channel, bank_psp_id=15):
        # if self.payment_transaction_sum_item:
        #     return self.payment_transaction_sum_item
        payment_transaction_sum_sql = 'SELECT * FROM `payment_transaction_sum` WHERE `bank_psp_id`="{bank_psp_id}" and work_date BETWEEN "{begin_date}" and "{end_date}"and pay_channel="{pay_channel}"'.format(
            bank_psp_id=bank_psp_id, begin_date=begin_date, end_date=end_date, pay_channel=channel)
        payment_transaction_sum_dict = SQLHelper.select_all(sql=payment_transaction_sum_sql,
                                                            connection_flag=ConnectionPool.SETTLEMENT)
        self.payment_transaction_sum_item = payment_transaction_sum_dict
        return self.payment_transaction_sum_item

    def get_sub_mch_data(self, begin_date, end_date, bank_psp_id=15):
        new_dict = {}
        # 首先计算微信的所有商户这段时间的交易
        for payment in self.payment_transaction_sum(begin_date=begin_date, end_date=end_date, channel='wechat'):
            if payment['mch_id'] in new_dict:
                info = new_dict.get(payment['mch_id'])
                info['transcation_count_wechat'] = info.get('transcation_count_wechat',0) + payment['pay_count'] + payment[
                    'refund_count'] + payment['revoked_count']
                info['transcation_fee_wechat'] = info.get('transcation_fee_wechat',0) + payment['transaction_fee']
            else:
                # 进行字典更新这个是每一个子商户的  将需要的字段更新到new_dict   #use_wechat #use_alipay #sub_mch_count #mdr_wechat #mdr_alipay
                try:
                    agency_id = self.get_mch_infos.get(payment['mch_id']).get('agency_id')
                    master_mch_id = self.get_mch_infos.get(payment['mch_id']).get('master_mch_id')

                    # 计算子商户自己的交易笔数和交易金额
                    transcation_count_wechat = payment['pay_count'] + payment['refund_count'] + payment['revoked_count']
                    transcation_fee_wechat = payment['transaction_fee']
                    new_dict[payment['mch_id']] = {
                        'master_mch_id': master_mch_id,
                        # 'agency_id': agency_id,
                        'transcation_count_wechat': transcation_count_wechat,
                        'transcation_fee_wechat': transcation_fee_wechat,
                    }
                except AttributeError as attrerror:
                    print(attrerror,payment['mch_id'],'子商户这里报错微信')
                    continue

        for payment in self.payment_transaction_sum(begin_date=begin_date, end_date=end_date, channel='alipay'):
            if payment['mch_id'] in new_dict:
                info = new_dict.get(payment['mch_id'])
                print(info)
                info['transcation_count_alipay'] = info.get('transcation_count_alipay',0) + payment['pay_count'] + payment[
                    'refund_count'] + payment['revoked_count']
                info['transcation_fee_alipay'] = info.get('transcation_fee_alipay',0) + payment['transaction_fee']
            else:
                # 进行字典更新这个是每一个子商户的  将需要的字段更新到new_dict   #use_wechat #use_alipay #sub_mch_count #mdr_wechat #mdr_alipay
                try:
                    agency_id = self.get_mch_infos.get(payment['mch_id']).get('agency_id')
                    master_mch_id = self.get_mch_infos.get(payment['mch_id']).get('master_mch_id')

                    # 计算子商户自己的交易笔数和交易金额
                    transcation_count_alipay = payment['pay_count'] + payment['refund_count'] + payment['revoked_count']
                    transcation_fee_alipay = payment['transaction_fee']
                    new_dict[payment['mch_id']] = {
                        'master_mch_id': master_mch_id,
                        # 'agency_id': agency_id,
                        'transcation_count_alipay': transcation_count_alipay,
                        'transcation_fee_alipay': transcation_fee_alipay,
                    }
                except AttributeError as attrerror:
                    print(attrerror, payment['mch_id'], '子商户这里报错支付宝')
                    continue

        return new_dict

    def get_master_data(self, begin_date, end_date, bank_psp_id=15):
        new_dict = {}
        for key, val in self.get_sub_mch_data(begin_date=begin_date, end_date=end_date).items():
            print(key, val)
            if val['master_mch_id'] in new_dict:
                info = new_dict[val['master_mch_id']]
                # 将交易笔数进行累计
                info['transcation_count_wechat'] = val.get('transcation_count_wechat',0) + info['transcation_count_wechat']
                info['transcation_count_alipay'] =val.get('transcation_count_alipay',0) + info['transcation_count_alipay']
                # 交易金额进行累计
                info['transcation_fee_wechat'] = val.get('transcation_fee_wechat',0) + info['transcation_fee_wechat']
                info['transcation_fee_alipay'] = val.get('transcation_fee_alipay',0) + info['transcation_fee_alipay']


            else:
                try:
                    use_wechat = self.get_mch_infos.get(val['master_mch_id']).get('use_wechat')
                    use_alipay = self.get_mch_infos.get(val['master_mch_id']).get('use_alipay')
                    sub_mch_count = len([mch for mch, values in self.get_mch_infos.items() if
                                         values['master_mch_id'] == val['master_mch_id'] and values[
                                             'is_master_mch'] == 'N' and
                                         values['create_time'].strftime('%Y-%m-%d') <= end_date])
                    mdr_wechat = [mch_fee_rate for mch_fee_rate in self.mch_fee_rate_flow if
                                  mch_fee_rate['mch_id'] == val['master_mch_id'] and mch_fee_rate[
                                      'channel_id'] == "wechat"]
                    if mdr_wechat:
                        mdr_wechat = mdr_wechat[0]['ksher_fee_rate']
                    else:
                        mdr_wechat = -1
                    mdr_alipay = [mch_fee_rate for mch_fee_rate in self.mch_fee_rate_flow if
                                  mch_fee_rate['mch_id'] == val['master_mch_id'] and mch_fee_rate[
                                      'channel_id'] == "alipay"]
                    if mdr_alipay:
                        mdr_alipay = mdr_alipay[0]['ksher_fee_rate']
                    else:
                        mdr_alipay = -1
                    # 付商户的交易笔数做记录
                    transcation_count_wechat = val.get('transcation_count_wechat', 0)
                    transcation_count_alipay = val.get('transcation_count_alipay', 0)

                    transcation_fee_alipay = val.get('transcation_fee_alipay', 0)
                    transcation_fee_wechat = val.get('transcation_fee_wechat', 0)
                    # 从配置文件中找到对应的agency_mdr
                    agency_id = self.get_mch_infos.get(val['master_mch_id']).get('agency_id')
                    if str(agency_id) not in other_config:
                        # 不在配置文件中说明是其他渠道  取other的费率进行更新
                        agency_wechat = other_config.get('0').get('wechat')
                        agency_alipay = other_config.get('0').get('alipay')
                        mdr_agency_wechat = agency_wechat.get('mdr_agency')
                        mdr_cost_wechat = agency_wechat.get('mdr_cost')
                        mdr_factor_wechat = agency_wechat.get('factor')
                        mdr_agency_alipay = agency_alipay.get('mdr_agency')
                        mdr_cost_alipay = agency_alipay.get('mdr_cost')
                        mdr_factor_alipay = agency_alipay.get('factor')
                        use_master_mdr_wechat = 'N'
                        use_master_mdr_alipay = 'N'
                    else:
                        agency_wechat = other_config.get(str(agency_id)).get('wechat')
                        agency_alipay = other_config.get(str(agency_id)).get('alipay')
                        if agency_wechat.get('use_master_mdr_wechat') == 'Y':
                            mdr_agency_wechat = mdr_wechat
                            use_master_mdr_wechat = 'Y'
                        else:
                            mdr_agency_wechat = agency_wechat.get('mdr_agency')
                            use_master_mdr_wechat = 'N'
                        if agency_alipay.get('use_master_mdr_alipay') == 'Y':
                            mdr_agency_alipay = mdr_alipay
                            use_master_mdr_alipay = 'Y'
                        else:
                            mdr_agency_alipay = agency_alipay.get('mdr_agency')
                            use_master_mdr_alipay = 'N'
                        mdr_cost_alipay = agency_alipay.get('mdr_cost')
                        mdr_factor_alipay = agency_alipay.get('factor')
                        mdr_cost_wechat = agency_wechat.get('mdr_cost')
                        mdr_factor_wechat = agency_wechat.get('factor')
                    new_dict[val['master_mch_id']] = {}
                    new_dict[val['master_mch_id']]['begin_date'] = begin_date
                    new_dict[val['master_mch_id']]['end_date'] = end_date
                    new_dict[val['master_mch_id']]['agency_id'] = agency_id
                    new_dict[val['master_mch_id']]['master_mch_id'] = val['master_mch_id']
                    new_dict[val['master_mch_id']]['sub_mch_count'] = sub_mch_count
                    new_dict[val['master_mch_id']]['use_wechat'] = use_wechat
                    new_dict[val['master_mch_id']]['use_alipay'] = use_alipay
                    new_dict[val['master_mch_id']]['mdr_wechat'] = mdr_wechat
                    new_dict[val['master_mch_id']]['mdr_alipay'] = mdr_alipay
                    new_dict[val['master_mch_id']]['transcation_count_wechat'] = transcation_count_wechat
                    new_dict[val['master_mch_id']]['transcation_count_alipay'] = transcation_count_alipay
                    new_dict[val['master_mch_id']]['transcation_fee_wechat'] = transcation_fee_wechat
                    new_dict[val['master_mch_id']]['transcation_fee_alipay'] = transcation_fee_alipay
                    new_dict[val['master_mch_id']]['mdr_agency_wechat'] = mdr_agency_wechat
                    new_dict[val['master_mch_id']]['mdr_agency_alipay'] = mdr_agency_alipay
                    new_dict[val['master_mch_id']]['mdr_cost_wechat'] = mdr_cost_wechat
                    new_dict[val['master_mch_id']]['factor_wechat'] = mdr_factor_wechat
                    new_dict[val['master_mch_id']]['use_master_mdr_wechat'] = use_master_mdr_wechat
                    new_dict[val['master_mch_id']]['mdr_agency_alipay'] = mdr_agency_alipay
                    new_dict[val['master_mch_id']]['mdr_cost_alipay'] = mdr_cost_alipay
                    new_dict[val['master_mch_id']]['factor_alipay'] = mdr_factor_alipay
                    new_dict[val['master_mch_id']]['use_master_mdr_alipay'] = use_master_mdr_alipay
                    new_dict[val['master_mch_id']]['bank_psp_id'] = bank_psp_id
                except AttributeError as attrerror:
                    print(attrerror,val['master_mch_id'],'父商户这里出错了')
                    continue
        # print(new_dict)

        # 计算银行收益
        for key, val in new_dict.items():
            # 当前收益
            agency_profit_wechat = ((val['transcation_fee_wechat'] / 100) * (
                    (float(val['mdr_agency_wechat']) - val['mdr_cost_wechat']) / 100) * val['factor_wechat']) * 100
            print(val['transcation_fee_wechat'],val['mdr_agency_wechat'],val['mdr_cost_wechat'],val['factor_wechat'])
            agency_profit_alipay = (val['transcation_fee_alipay'] /100 * (
                    (float(val['mdr_agency_alipay']) - val['mdr_cost_alipay']) / 100) * val['factor_alipay']) * 100
            new_dict[key]['agency_profit_wechat'] = agency_profit_wechat
            new_dict[key]['agency_profit_alipay'] = agency_profit_alipay
        print(new_dict)
        for key, val in new_dict.items():
            self.insert_data(data=val)

    def insert_data(self, data):
        sql = 'select * from week_transaction_report where begin_date="{}" and end_date="{}" and master_mch_id="{}"'.format(
            data['begin_date'], data['end_date'], data['master_mch_id'])
        row_count = SQLHelper.insert(sql=sql, args=None, connection_flag=ConnectionPool.SETTLEMENT)
        if row_count:
            pass
        else:
            sql = 'INSERT INTO `week_transaction_report`' \
                  ' (`bank_psp_id`,' \
                  '`begin_date`,' \
                  '`end_date`,' \
                  '`agency_id`,' \
                  '`master_mch_id`,' \
                  '`sub_mch_count`,' \
                  '`use_wechat`,' \
                  '`mdr_wechat`,' \
                  '`use_alipay`,' \
                  '`mdr_alipay`,' \
                  '`transcation_count_wechat`,' \
                  '`transcation_count_alipay`,' \
                  '`transcation_fee_wechat`,' \
                  '`transcation_fee_alipay`,' \
                  '`mdr_agency_wechat`,' \
                  '`mdr_cost_wechat`,' \
                  '`factor_wechat`,' \
                  '`use_master_mdr_wechat`,' \
                  '`mdr_agency_alipay`,' \
                  '`mdr_cost_alipay`,' \
                  '`factor_alipay`,' \
                  '`use_master_mdr_alipay`,' \
                  '`agency_profit_wechat`,' \
                  '`agency_profit_alipay`) VALUES ("{bank_psp_id}",' \
                  '"{begin_date}",' \
                  '"{end_date}",' \
                  '"{agency_id}",' \
                  '"{master_mch_id}",' \
                  '"{sub_mch_count}",' \
                  '"{use_wechat}",' \
                  '"{mdr_wechat}",' \
                  '"{use_alipay}",' \
                  '"{mdr_alipay}",' \
                  '"{transcation_count_wechat}",' \
                  '"{transcation_count_alipay}",' \
                  '"{transcation_fee_wechat}",' \
                  '"{transcation_fee_alipay}",' \
                  '"{mdr_agency_wechat}",' \
                  '"{mdr_cost_wechat}",' \
                  '"{factor_wechat}",' \
                  '"{use_master_mdr_wechat}",' \
                  '"{mdr_agency_alipay}",' \
                  '"{mdr_cost_alipay}",' \
                  '"{factor_alipay}",' \
                  '"{use_master_mdr_alipay}",' \
                  '"{agency_profit_wechat}",' \
                  '"{agency_profit_alipay}")'.format(**data)
            try:
                SQLHelper.insert(sql=sql, args=None, connection_flag=ConnectionPool.SETTLEMENT)
            except Exception as e:
                print(e)


# if __name__ == '__main__':
#     WeekReport().get_master_data(begin_date='2019-09-01', end_date='2019-09-15')
# base_config.get('JP_DAY_WEEK_RATE_CONFIG')
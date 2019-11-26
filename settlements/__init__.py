# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""

# def get_data(self, begin_date,end_date, bank_psp_id=15):
#     new_dict = {}
#     for payment in self.payment_transaction_sum(begin_date=begin_date,end_date=end_date, channel="wechat"):
#         if payment['mch_id'] in new_dict:
#             info = new_dict.get(payment['mch_id'])
#             info['transcation_count_wechat'] = info['transcation_count_wechat'] + payment['pay_count'] + payment[
#                 'refund_count'] + payment['revoked_count']
#             info['transcation_fee_wechat'] = info['transcation_fee_wechat'] + payment['transaction_fee']
#         else:
#             agency_id = self.get_mch_infos.get(payment['mch_id']).get('agency_id')
#             try:
#                 agency_name = self.get_agencies.get(agency_id).get('name')
#             except Exception:
#                 agency_name = ''
#             master_mch_id = self.get_mch_infos.get(payment['mch_id']).get('master_mch_id')
#             master_mch_name = self.get_mch_infos.get(
#                 self.get_mch_infos.get(payment['mch_id']).get('master_mch_id')).get('mch_name_local')
#             mch_name_local = self.get_mch_infos.get(payment['mch_id']).get('mch_name_local')
#             try:
#                 mdr_agency_wechat = other_config.get('agency_id').get('wechat').get('mdr_agency')
#             except Exception:
#                 mdr_agency_wechat = None
#             if not mdr_agency_wechat:
#                 mdr_agency_wechat = [mch_fee_rate for mch_fee_rate in self.mch_fee_rate_flow if
#                                      mch_fee_rate['mch_id'] == payment['mch_id'] and mch_fee_rate[
#                                          'channel_id'] == "wechat"]
#                 if mdr_agency_wechat:
#                     mdr_agency_wechat = mdr_agency_wechat[0]['ksher_fee_rate']
#                 else:
#                     mdr_agency_wechat = 0
#             try:
#                 mdr_agency_alipay = other_config.get('agency_id').get('alipay').get('mdr_agency')
#             except Exception:
#                 mdr_agency_alipay = None
#             if not mdr_agency_alipay:
#                 mdr_agency_alipay = [mch_fee_rate for mch_fee_rate in self.mch_fee_rate_flow if
#                                      mch_fee_rate['mch_id'] == payment['mch_id'] and mch_fee_rate[
#                                          'channel_id'] == "alipay"]
#                 if mdr_agency_alipay:
#                     mdr_agency_alipay = mdr_agency_alipay[0]['ksher_fee_rate']
#                 else:
#                     mdr_agency_alipay = 0
#             transcation_count_wechat = payment['pay_count'] + payment['refund_count'] + payment['revoked_count']
#             transcation_fee_wechat = payment['transaction_fee']
#             new_dict[payment['mch_id']] = {'mch_id': payment['mch_id'], 'agency_id': agency_id,
#                                            'agency_name': agency_name, 'master_mch_id': master_mch_id,
#                                            'master_mch_name': master_mch_name, 'mch_name_local': mch_name_local,
#                                            'mdr_agency_wechat': mdr_agency_wechat,
#                                            'mdr_agency_alipay': mdr_agency_alipay,
#                                            'transcation_count_wechat': transcation_count_wechat,
#                                            'transcation_fee_wechat': transcation_fee_wechat,
#                                            'bank_psp_id': bank_psp_id,
#                                            'transcation_count_alipay': 0,
#                                            'transcation_fee_alipay': 0,
#                                            'date': date
#                                            }
#     for payment in self.payment_transaction_sum(begin_date=begin_date,end_date=end_date, channel="alipay"):
#         if payment['mch_id'] in new_dict:
#             info = new_dict.get(payment['mch_id'])
#             info['transcation_count_alipay'] = info['transcation_count_alipay'] + payment['pay_count'] + payment[
#                 'refund_count'] + payment['revoked_count']
#             info['transcation_fee_alipay'] = info['transcation_fee_alipay'] + payment['transaction_fee']
#         else:
#             agency_id = self.get_mch_infos.get(payment['mch_id']).get('agency_id')
#             try:
#                 agency_name = self.get_agencies.get(agency_id).get('name')
#             except Exception:
#                 agency_name = ''
#             master_mch_id = self.get_mch_infos.get(payment['mch_id']).get('master_mch_id')
#             master_mch_name = self.get_mch_infos.get(
#                 self.get_mch_infos.get(payment['mch_id']).get('master_mch_id')).get('mch_name_local')
#             mch_name_local = self.get_mch_infos.get(payment['mch_id']).get('mch_name_local')
#             try:
#                 mdr_agency_wechat = other_config.get('agency_id').get('wechat').get('mdr_agency')
#             except Exception:
#                 mdr_agency_wechat = None
#             if not mdr_agency_wechat:
#                 mdr_agency_wechat = [mch_fee_rate for mch_fee_rate in self.mch_fee_rate_flow if
#                                      mch_fee_rate['mch_id'] == payment['mch_id'] and mch_fee_rate[
#                                          'channel_id'] == "wechat"]
#                 if mdr_agency_wechat:
#                     mdr_agency_wechat = mdr_agency_wechat[0]['ksher_fee_rate']
#                 else:
#                     mdr_agency_wechat = 0
#             try:
#                 mdr_agency_alipay = other_config.get('agency_id').get('alipay').get('mdr_agency')
#             except:
#                 mdr_agency_alipay = None
#             if not mdr_agency_alipay:
#                 mdr_agency_alipay = [mch_fee_rate for mch_fee_rate in self.mch_fee_rate_flow if
#                                      mch_fee_rate['mch_id'] == payment['mch_id'] and mch_fee_rate[
#                                          'channel_id'] == "alipay"]
#                 if mdr_agency_alipay:
#                     mdr_agency_alipay = mdr_agency_alipay[0]['ksher_fee_rate']
#                 else:
#                     mdr_agency_alipay = 0
#                 transcation_count_alipay = payment['pay_count'] + payment['refund_count'] + payment['revoked_count']
#                 transcation_fee_alipay = payment['transaction_fee']
#                 new_dict[payment['mch_id']] = {'mch_id': payment['mch_id'], 'agency_id': agency_id,
#                                                'agency_name': agency_name, 'master_mch_id': master_mch_id,
#                                                'master_mch_name': master_mch_name, 'mch_name_local': mch_name_local,
#                                                'mdr_agency_wechat': mdr_agency_wechat,
#                                                'mdr_agency_alipay': mdr_agency_alipay,
#                                                'transcation_count_wechat': 0,
#                                                'transcation_fee_wechat': 0,
#                                                'bank_psp_id': bank_psp_id,
#                                                'transcation_count_alipay': transcation_count_alipay,
#                                                'transcation_fee_alipay': transcation_fee_alipay,
#                                                'date': date
#                                                }
#     # 开始计算每日银行的收益
#     for key, val in new_dict.items():
#         try:
#             mdr_cost_wechat = other_config[val['agency_id']]['wechat']['mdr_cost']
#         except Exception as e:
#             mdr_cost_wechat = 0.5
#         try:
#             mdr_cost_alipay = other_config[val['agency_id']]['alipay']['mdr_cost']
#         except Exception as e:
#             mdr_cost_alipay = 0.8
#         try:
#             alipay_factor = other_config[val['agency_id']]['alipay']['factor']
#         except Exception:
#             alipay_factor = 0.45
#         try:
#             wechat_factor = other_config[val['agency_id']]['alipay']['factor']
#         except Exception:
#             wechat_factor = 0.45
#         new_dict[key]['bank_fee_wechat'] = (val['transcation_fee_wechat'] / 100) * (
#                     ((float(val['mdr_agency_wechat']) - mdr_cost_wechat) / 100) * wechat_factor)
#         new_dict[key]['bank_fee_alipay'] = (val['transcation_fee_alipay'] / 100) * (
#                 ((float(val['mdr_agency_alipay']) - mdr_cost_alipay) / 100) * alipay_factor)
#
#     print(new_dict)
#     # 调用插入数据
#     for key, val in new_dict.items():
#         print(val)
#         #     self.insert_data(date=date,mch_id=key,data=val)
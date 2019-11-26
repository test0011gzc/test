from settlements.sqlhelper import SQLHelper, ConnectionPool
from settlements.report.create_day_excel import create_day_excel
from settlements.report.create_week_excel import create_week_excel


class DayResult(object):

    def get_data(self, date):
        sql = 'select * from day_transaction_report where transaction_date<="{}" order by transaction_date asc '.format(date)
        row_dicts = SQLHelper.select_all(sql=sql, connection_flag=ConnectionPool.SETTLEMENT)
        datalist = []
        for row_dict in row_dicts:
            data = {
                'use_wechat':row_dict.get('use_wechat'),
                'use_alipay':row_dict.get('use_alipay'),
                'date': row_dict.get('transaction_date'),
                'master_mch_count': row_dict.get('master_mch_count'),
                'sub_mch_count': row_dict.get('sub_mch_count'),
                'transaction_count': {
                    'wechat': int(row_dict.get('transaction_count_wechat')),
                    'alipay': int(row_dict.get('transaction_count_alipay')),
                    'wechat+alipay': int(row_dict.get('transaction_count_wechat')) + int(row_dict.get('transaction_count_alipay'))
                },
                'transaction_fee': {
                    'wechat': int(round(row_dict.get('transaction_fee_wechat')/100,0)),
                    'alipay': int(round(row_dict.get('transaction_fee_alipay')/100,0)),
                    'wechat+alipay': int(round(row_dict.get('transaction_fee_wechat')/100,0)) + int(round(row_dict.get('transaction_fee_alipay')/100,0))
                }
            }
            datalist.append(data)
        print(datalist)
        try:
            create_day_excel(stub_data=datalist)
        except Exception as e:
            print(e)




class WeekResult(object):
    agency_dict = None
    mch_info_dict = None

    @property
    def get_mch_infos(self, bank_psp_id=15):
        if self.mch_info_dict:
            return self.mch_info_dict
        mch_info_sql = 'SELECT * FROM `mch_info` WHERE `bank_psp_id`="{}"'.format(bank_psp_id)
        self.mch_info_dict = {mch['mch_id']: mch for mch in SQLHelper.select_all(sql=mch_info_sql)}
        return self.mch_info_dict

    @property
    def get_agencies(self):
        if self.agency_dict:
            return self.agency_dict
        agency_sql = 'SELECT * FROM `agencies`'
        self.agency_dict = {agency['id']: agency for agency in SQLHelper.select_all(sql=agency_sql)}
        return self.agency_dict

    def get_data(self, begin_date, end_date):
        sql = 'select * from week_transaction_report where begin_date="{}" and end_date="{}"'.format(begin_date,
                                                                                                     end_date)
        row_dict = SQLHelper.select_all(sql=sql, connection_flag=ConnectionPool.SETTLEMENT)
        data = {
            'total_count': len(row_dict),
            'begin_date': begin_date,
            'end_date': end_date,
            'data': []
        }

        for row in row_dict:
            new_dict = {}
            for agency in data['data']:
                if agency['agency_id'] == row['agency_id']:
                    agency['count'] += 1
                    agency['data_list'].append(
                        {
                            'master_mch_id': row['master_mch_id'],
                            'master_mch_name': self.get_mch_infos.get(str(row['master_mch_id'])).get('mch_name'),
                            'sub_mch_count': row['sub_mch_count'],
                            'mdr': {
                                'wechat': row['mdr_wechat'],
                                'alipay': row['mdr_alipay'],
                            },
                            'transaction_count': {
                                'wechat': int(row['transcation_count_wechat']),
                                'alipay': int(row['transcation_count_alipay']),
                                'wechat+alipay': int(row['transcation_count_wechat'] + row['transcation_count_alipay'])
                            },
                            'transaction_fee': {
                                'wechat': int(round(row['transcation_fee_wechat']/100,0)),
                                'alipay': int(round(row['transcation_fee_alipay']/100,0)),
                                'wechat+alipay': int(round(row['transcation_fee_wechat']/100,0) + round(row['transcation_fee_alipay']/100,0))
                            },
                            'agency_profit': {
                                'wechat': round(row['agency_profit_wechat']/100,0),
                                'alipay': round(row['agency_profit_alipay']/100,0),
                                'wechat+alipay': int(round(row['agency_profit_wechat']/100,0) + round(row['agency_profit_alipay']/100,0))
                            }
                        }
                    )
                    break
            else:
                new_dict['agency_id'] = row['agency_id']
                new_dict['agency_name'] = self.get_agencies.get(row['agency_id']).get('name') if self.get_agencies.get(row['agency_id']) else ''
                new_dict['count'] = 1
                new_dict['data_list'] = [{
                    'master_mch_id':row['master_mch_id'],
                    'master_mch_name':self.get_mch_infos.get(str(row['master_mch_id'])).get('mch_name'),
                    'sub_mch_count':row['sub_mch_count'],
                    'mdr':{
                        'wechat':row['mdr_wechat'],
                        'alipay':row['mdr_alipay'],
                    },
                    'transaction_count':{
                        'wechat':int(row['transcation_count_wechat']),
                        'alipay':int(row['transcation_count_alipay']),
                        'wechat+alipay': int(row['transcation_count_wechat'] + row['transcation_count_alipay'])
                    },
                    'transaction_fee': {
                        'wechat': int(round(row['transcation_fee_wechat']/100,0)),
                        'alipay': int(round(row['transcation_fee_alipay']/100,0)),
                        'wechat+alipay': int(round(row['transcation_fee_wechat']/100,0) + round(row['transcation_fee_alipay']/100,0))
                    },
                    'agency_profit': {
                        'wechat': int(round(row['agency_profit_wechat']/100,0)),
                        'alipay': int(round(row['agency_profit_alipay']/100,0)),
                        'wechat+alipay': int(round(row['agency_profit_wechat']/100,0) + round(row['agency_profit_alipay']/100,0))
                    }
                }]
                data['data'].append(new_dict)
        print(data)
        # try:
        #     create_week_excel(stub_data=data)
        # except Exception as e:
        #     print(e)
        create_week_excel(stub_data=data)


# if __name__ == '__main__':
#     DayResult().get_data('2019-10-10')
    # WeekResult().get_data(begin_date='2019-09-01', end_date='2019-11-15')

# class A:
#     def __init__(self):
#         super().__init__()
#
#     def __new__(cls, *args, **kwargs):
#         return super().__new__(cls, *args, **kwargs)
#
#     def __call__(self, *args, **kwargs):
#         print('11111111')
# a = A()
# if callable(a):
#     print(a())
# else:
#     print(a)
#
# import flask
#
# app = flask.Flask(__name__)
#
# app.run()

# a = '''
# 2188
# 99
# 259
# 10
# 261
# 0
# 46
# 158
# 54685
# 13572
# 282
# 992
# 2994
# 1310
# 140
# 750
# 243
# 1639
# 13
# 74
# 129
# 79846
# '''
# b = a.split('\n')
# print(b)

data = {
    'total_count': 17,
    'begin_date': '2019-09-01',
    'end_date': '2019-09-15',
    'data': [{
        'agency_id': 10204,
        'agency_name': '楽天银行',
        'count': 9,
        'data_list': [{
            'master_mch_id': 27593,
            'master_mch_name': '株式会社福岡デューティーフリー',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('1.10'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 974,
                'alipay': 0,
                'wechat+alipay': 974
            },
            'transaction_fee': {
                'wechat': 21138744,
                'alipay': 0,
                'wechat+alipay': 21138744
            },
            'agency_profit': {
                'wechat': 57075,
                'alipay': 0,
                'wechat+alipay': 57075
            }
        }, {
            'master_mch_id': 27128,
            'master_mch_name': 'タワーレコード株式会社',
            'sub_mch_count': 6,
            'mdr': {
                'wechat': Decimal('2.05'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 129,
                'alipay': 0,
                'wechat+alipay': 129
            },
            'transaction_fee': {
                'wechat': 826026,
                'alipay': 0,
                'wechat+alipay': 826026
            },
            'agency_profit': {
                'wechat': 5762.0,
                'alipay': 0.0,
                'wechat+alipay': 5762
            }
        }, {
            'master_mch_id': 26968,
            'master_mch_name': '寿味屋食品株式会社',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('1.60'),
                'alipay': Decimal('1.80')
            },
            'transaction_count': {
                'wechat': 17,
                'alipay': 7,
                'wechat+alipay': 24
            },
            'transaction_fee': {
                'wechat': 27406,
                'alipay': 16360,
                'wechat+alipay': 43766
            },
            'agency_profit': {
                'wechat': 136.0,
                'alipay': 74.0,
                'wechat+alipay': 210
            }
        }, {
            'master_mch_id': 27144,
            'master_mch_name': '株式会社バロックジャパンリミテッド',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('2.10'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 12,
                'alipay': 0,
                'wechat+alipay': 12
            },
            'transaction_fee': {
                'wechat': 75506,
                'alipay': 0,
                'wechat+alipay': 75506
            },
            'agency_profit': {
                'wechat': 544.0,
                'alipay': 0.0,
                'wechat+alipay': 544
            }
        }, {
            'master_mch_id': 26964,
            'master_mch_name': '株式会社沖縄県物産公社',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('1.60'),
                'alipay': Decimal('1.80')
            },
            'transaction_count': {
                'wechat': 1,
                'alipay': 5,
                'wechat+alipay': 6
            },
            'transaction_fee': {
                'wechat': 1674,
                'alipay': 7702,
                'wechat+alipay': 9376
            },
            'agency_profit': {
                'wechat': 8.0,
                'alipay': 35.0,
                'wechat+alipay': 43
            }
        }, {
            'master_mch_id': 27139,
            'master_mch_name': '株式会社\u3000ホイッスル三好',
            'sub_mch_count': 2,
            'mdr': {
                'wechat': Decimal('1.75'),
                'alipay': Decimal('1.75')
            },
            'transaction_count': {
                'wechat': 22,
                'alipay': 0,
                'wechat+alipay': 22
            },
            'transaction_fee': {
                'wechat': 61970,
                'alipay': 0,
                'wechat+alipay': 61970
            },
            'agency_profit': {
                'wechat': 349.0,
                'alipay': 0.0,
                'wechat+alipay': 349
            }
        }, {
            'master_mch_id': 26966,
            'master_mch_name': '株式会社沖縄県物産公社',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('1.60'),
                'alipay': Decimal('1.80')
            },
            'transaction_count': {
                'wechat': 4,
                'alipay': 19,
                'wechat+alipay': 23
            },
            'transaction_fee': {
                'wechat': 5060,
                'alipay': 41317,
                'wechat+alipay': 46377
            },
            'agency_profit': {
                'wechat': 25.0,
                'alipay': 186.0,
                'wechat+alipay': 211
            }
        }, {
            'master_mch_id': 26917,
            'master_mch_name': '株式会社三陽商会 ',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('2.00'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 7,
                'alipay': 0,
                'wechat+alipay': 7
            },
            'transaction_fee': {
                'wechat': 362510,
                'alipay': 0,
                'wechat+alipay': 362510
            },
            'agency_profit': {
                'wechat': 2447.0,
                'alipay': 0.0,
                'wechat+alipay': 2447
            }
        }, {
            'master_mch_id': 27141,
            'master_mch_name': '株式会社Ｉ－ｎｅ',
            'sub_mch_count': 2,
            'mdr': {
                'wechat': Decimal('2.50'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 1,
                'alipay': 0,
                'wechat+alipay': 1
            },
            'transaction_fee': {
                'wechat': 1836,
                'alipay': 0,
                'wechat+alipay': 1836
            },
            'agency_profit': {
                'wechat': 17.0,
                'alipay': 0.0,
                'wechat+alipay': 17
            }
        }]
    }, {
        'agency_id': 10186,
        'agency_name': '楽天ペイメント株式会社',
        'count': 2,
        'data_list': [{
            'master_mch_id': 27263,
            'master_mch_name': '株式会社ステップ',
            'sub_mch_count': 98,
            'mdr': {
                'wechat': Decimal('2.60'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 27,
                'alipay': 0,
                'wechat+alipay': 27
            },
            'transaction_fee': {
                'wechat': 467970,
                'alipay': 0,
                'wechat+alipay': 467970
            },
            'agency_profit': {
                'wechat': 2527,
                'alipay': 0,
                'wechat+alipay': 2527
            }
        }, {
            'master_mch_id': 27264,
            'master_mch_name': '株式会社西川 ',
            'sub_mch_count': 2,
            'mdr': {
                'wechat': Decimal('3.24'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 2,
                'alipay': 0,
                'wechat+alipay': 2
            },
            'transaction_fee': {
                'wechat': 116500,
                'alipay': 0,
                'wechat+alipay': 116500
            },
            'agency_profit': {
                'wechat': 629.0,
                'alipay': 0.0,
                'wechat+alipay': 629
            }
        }]
    }, {
        'agency_id': 10203,
        'agency_name': 'Snプロパティーマネジメント株式会社',
        'count': 1,
        'data_list': [{
            'master_mch_id': 27293,
            'master_mch_name': 'ボルコムジャパン\u3000合同会社',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('2.65'),
                'alipay': Decimal('2.65')
            },
            'transaction_count': {
                'wechat': 2,
                'alipay': 0,
                'wechat+alipay': 2
            },
            'transaction_fee': {
                'wechat': 11903,
                'alipay': 0,
                'wechat+alipay': 11903
            },
            'agency_profit': {
                'wechat': 62,
                'alipay': 0,
                'wechat+alipay': 62
            }
        }]
    }, {
        'agency_id': 10201,
        'agency_name': '株式会社マネーパートナーズソリューションズ',
        'count': 2,
        'data_list': [{
            'master_mch_id': 27294,
            'master_mch_name': '株式会社まるごとにっぽん',
            'sub_mch_count': 39,
            'mdr': {
                'wechat': Decimal('2.90'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 8,
                'alipay': 0,
                'wechat+alipay': 8
            },
            'transaction_fee': {
                'wechat': 22294,
                'alipay': 0,
                'wechat+alipay': 22294
            },
            'agency_profit': {
                'wechat': 130,
                'alipay': 0,
                'wechat+alipay': 130
            }
        }, {
            'master_mch_id': 27565,
            'master_mch_name': '有限会社浅草たこ丸',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('2.90'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 17,
                'alipay': 0,
                'wechat+alipay': 17
            },
            'transaction_fee': {
                'wechat': 15000,
                'alipay': 0,
                'wechat+alipay': 15000
            },
            'agency_profit': {
                'wechat': 88.0,
                'alipay': 0.0,
                'wechat+alipay': 88
            }
        }]
    }, {
        'agency_id': 10202,
        'agency_name': 'サッポログループマネジメント株式会社',
        'count': 2,
        'data_list': [{
            'master_mch_id': 27282,
            'master_mch_name': '株式会社\u3000新星苑',
            'sub_mch_count': 1,
            'mdr': {
                'wechat': Decimal('1.90'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 16,
                'alipay': 0,
                'wechat+alipay': 16
            },
            'transaction_fee': {
                'wechat': 24471,
                'alipay': 0,
                'wechat+alipay': 24471
            },
            'agency_profit': {
                'wechat': 143,
                'alipay': 0,
                'wechat+alipay': 143
            }
        }, {
            'master_mch_id': 27258,
            'master_mch_name': '株式会社サッポロライオン',
            'sub_mch_count': 18,
            'mdr': {
                'wechat': Decimal('1.90'),
                'alipay': Decimal('-1.00')
            },
            'transaction_count': {
                'wechat': 5,
                'alipay': 0,
                'wechat+alipay': 5
            },
            'transaction_fee': {
                'wechat': 26291,
                'alipay': 0,
                'wechat+alipay': 26291
            },
            'agency_profit': {
                'wechat': 154.0,
                'alipay': 0.0,
                'wechat+alipay': 154
            }
        }]
    }, {
        'agency_id': 10200,
        'agency_name': 'シグニチャージャパン株式会社',
        'count': 1,
        'data_list': [{
            'master_mch_id': 26404,
            'master_mch_name': '株式会社近鉄・都ホテルズ',
            'sub_mch_count': 2,
            'mdr': {
                'wechat': Decimal('1.90'),
                'alipay': Decimal('1.90')
            },
            'transaction_count': {
                'wechat': 1,
                'alipay': 3,
                'wechat+alipay': 4
            },
            'transaction_fee': {
                'wechat': 16200,
                'alipay': 21797,
                'wechat+alipay': 37997
            },
            'agency_profit': {
                'wechat': 95,
                'alipay': 98,
                'wechat+alipay': 193
            }
        }]
    }]
}

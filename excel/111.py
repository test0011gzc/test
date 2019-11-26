# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""

# {
#     'file_name': '/path/to/xyz.xlsx',
#     'auto_span': False,
#     'sheet_list':[
#         {
#             'sheet_name': 'sheet1',
#             'data': [
#                 {
#                     'start_row': 1,
#                     'start_column': 1,
#                     'info':[
#                         [{'content': 'mch_id', 'format': None}, {'content': 'bank_id', 'format': None}]
#                         [{'content': '20015', 'format': None}, {'content': '1001', 'format': None}]
#                     ]
#                 },
#                 {
#                     'start_row': 5,
#                     'start_column': 4,
#                     'info':[
#                         [{'content': 'summary', 'format': None}, {'content': 'total', 'format': None},{'content': 'fee_type', 'format': None}]
#                         [{'content': '2', 'format': None}, {'content': '300', 'format': None},{'content': 'THB', 'format': None}]
#                     ]
#                 }
#             ]
#         },
#
#         {
#             'sheet_name': 'sheet2',
#             'data': [
#                 {
#                     'start_row': 3,
#                     'start_column': 3,
#                     'info':[
#                         [{'content': 'mch_id', 'format': None}, {'content': 'bank_id', 'format': None}]
#                         [{'content': '20015', 'format': None}, {'content': '1001', 'format': None}]
#                     ]
#                 },
#                 {
#                     'start_row': 7,
#                     'start_column': 1,
#                     'info':[
#                         [{'content': 'summary', 'format': None}, {'content': 'total', 'format': None},{'content': 'fee_type', 'format': None}]
#                         [{'content': '2', 'format': None}, {'content': '300', 'format': None},{'content': 'THB', 'format': None}]
#                     ]
#                 }
#             ]
#         }
#     ]
# }

res = {
    'filename': 'test_excel.xlsx',
    'start_row': 0,
    'start_col': 0,
    'sheet_name': 'hahahah',
    'alignment': True,
    'data': [
        {
            'info': [
                [
                    {
                        'content': '学生',
                        'format': {
                            'align': 'center',
                        }
                    },
                    {
                        'content': '班级',
                        'format': {
                            'color': 'red',
                            'align': 'center',
                        }
                    },
                    {
                        'content': '成绩url',
                        'format': {
                            'color': 'blank',
                        }
                    },
                ],
                [
                    {
                        'content': '巩志成',
                    },
                    {
                        'content': '1',
                        'format': {
                            'color': 'red',
                            'align': 'center',
                        }
                    },

                    {
                        'content': 'ksher.com',
                        'format': {
                            'color': '#DDA0DD',
                        }
                    },
                ],
                [
                    {
                        'content': '巩志成',
                    },
                    {
                        'content': '1',
                        'format': {
                            'color': 'red',
                            'align': 'center',
                        }
                    },

                    {
                        'content': 'https://www.sioe.cn/yingyong/yanse-rgb-16/',
                        'format': {
                            'color': '#DDA0DD',
                        }
                    },
                ],
                [
                    {
                        'content': '巩志成',
                    },
                    {
                        'content': '1',
                        'format': {
                            'color': 'red',
                            'align': 'center',
                        }
                    },

                    {
                        'content': 'https://github.com/pyenv/pyenv/blob/master/bin/pyenv',
                        'format': {
                            'color': '#DDA0DD',
                        }
                    },
                ],
                [
                    {
                        'content': '巩志成',
                    },
                    {
                        'content': '1',
                        'format': {
                            'color': 'red',
                            'align': 'center',
                        }
                    },

                    {
                        'content': 'https://www.baidu.com',
                        'format': {
                            'color': '#DDA0DD',
                        }
                    },
                ],
                [
                    {
                        'content': '巩志成',
                    },
                    {
                        'content': '1',
                        'format': {
                            'color': 'red',
                            'align': 'center',
                        }
                    },

                    {
                        'content': 'https://blog.csdn.net/qq_23387055/article/details/89706741',
                        'format': {
                            'color': '#DDA0DD',
                        }
                    },
                ],
            ]
        }
    ]
}
import xlsxwriter as xw


colm = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
        'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 'AF', 'AG', 'AH', 'AI', 'AJ', 'AK', 'AL', 'AM', 'AN', 'AO',
        'AP', 'AQ', 'AR', 'AS', 'AT', 'AU', 'AV', 'AW', 'AX', 'AY', 'AZ', 'BA', 'BB', 'BC', 'BD', 'BE', 'BF', 'BG',
        'BH', 'BI', 'BJ', 'BK', 'BL', 'BM', 'BN', 'BO', 'BP', 'BQ', 'BR', 'BS', 'BT', 'BU', 'BV', 'BW', 'BX', 'BY',
        'BZ', 'CA', 'CB', 'CC', 'CD', 'CE', 'CF', 'CG', 'CH', 'CI', 'CJ', 'CK', 'CL', 'CM', 'CN', 'CO', 'CP', 'CQ',
        'CR', 'CS', 'CT', 'CU', 'CV', 'CW', 'CX', 'CY', 'CZ', 'DA', 'DB', 'DC', 'DD', 'DE', 'DF', 'DG', 'DH', 'DI',
        'DJ', 'DK', 'DL', 'DM', 'DN', 'DO', 'DP', 'DQ', 'DR', 'DS', 'DT', 'DU', 'DV', 'DW', 'DX', 'DY', 'DZ', 'EA',
        'EB', 'EC', 'ED', 'EE', 'EF', 'EG', 'EH', 'EI', 'EJ', 'EK', 'EL', 'EM', 'EN', 'EO', 'EP', 'EQ', 'ER', 'ES',
        'ET', 'EU', 'EV', 'EW', 'EX', 'EY', 'EZ', 'FA', 'FB', 'FC', 'FD', 'FE', 'FF', 'FG', 'FH', 'FI', 'FJ', 'FK',
        'FL', 'FM', 'FN', 'FO', 'FP', 'FQ', 'FR', 'FS', 'FT', 'FU', 'FV', 'FW', 'FX', 'FY', 'FZ', 'GA', 'GB', 'GC',
        'GD', 'GE', 'GF', 'GG', 'GH', 'GI', 'GJ', 'GK', 'GL', 'GM', 'GN', 'GO', 'GP', 'GQ', 'GR', 'GS', 'GT', 'GU',
        'GV', 'GW', 'GX', 'GY', 'GZ']


class TestWriteExcel(object):

    def __init__(self):
        self.book = xw.Workbook()

    def len_byte(self, value):
        '''
        去计算当前的适应长度
        :param value:
        :return:
        '''
        length = len(value)
        utf8_length = len(value.encode('utf-8'))
        length = (utf8_length - length) / 2 + length
        return int(length)

    def write_excel(self, res):
        '''
        res 格式
        info中的每一个list表示一行
        使用xlwt集成  支持里面的所有样式
        res = {
                'filename': 'test_excel.xlsx',
                'start_row': 0,
                'start_col': 0,
                'sheet_name': 'hahahah',
                'alignment': False,
                'data': [
                    {
                        'info': [
                            [
                                {
                                    'content': '学生',
                                    'format': {
                                        'align': 'center',
                                    }
                                },
                                {
                                    'content': '班级',
                                    'format': {
                                        'color': 'red',
                                        'align': 'center',
                                    }
                                },
                                {
                                    'content': '成绩url',
                                    'format': {
                                        'color': 'blank',
                                    }
                                },
                            ],
                            [
                                {
                                    'content': '巩志成',
                                },
                                {
                                    'content': '1',
                                    'format': {
                                        'color': 'red',
                                        'align': 'center',
                                    }
                                },

                                {
                                    'content': 'ksher.com',
                                    'format': {
                                        'color': '#DDA0DD',
                                    }
                                },
                            ],
                            [
                                {
                                    'content': '巩志成',
                                },
                                {
                                    'content': '1',
                                    'format': {
                                        'color': 'red',
                                        'align': 'center',
                                    }
                                },

                                {
                                    'content': 'https://www.sioe.cn/yingyong/yanse-rgb-16/',
                                    'format': {
                                        'color': '#DDA0DD',
                                    }
                                },
                            ],
                            [
                                {
                                    'content': '巩志成',
                                },
                                {
                                    'content': '1',
                                    'format': {
                                        'color': 'red',
                                        'align': 'center',
                                    }
                                },

                                {
                                    'content': 'https://github.com/pyenv/pyenv/blob/master/bin/pyenv',
                                    'format': {
                                        'color': '#DDA0DD',
                                    }
                                },
                            ],
                            [
                                {
                                    'content': '巩志成',
                                },
                                {
                                    'content': '1',
                                    'format': {
                                        'color': 'red',
                                        'align': 'center',
                                    }
                                },

                                {
                                    'content': 'https://www.baidu.com',
                                    'format': {
                                        'color': '#DDA0DD',
                                    }
                                },
                            ],
                            [
                                {
                                    'content': '巩志成',
                                },
                                {
                                    'content': '1',
                                    'format': {
                                        'color': 'red',
                                        'align': 'center',
                                    }
                                },

                                {
                                    'content': 'https://blog.csdn.net/qq_23387055/article/details/89706741',
                                    'format': {
                                        'color': '#DDA0DD',
                                    }
                                },
                            ],
                        ]
                    }
                ]
            }
        :param res:
        :return:
        '''
        col_width = {}
        file_name = res.get('filename', 'test.xlsx')
        sheet_name = res.get('sheet_name', 'Sheet1')
        data = res.get('data', {})
        start_row = res.get('start_row', 0)
        start_col = res.get('start_col', 0)
        alignment = res.get('alignment', False)
        self.book.filename = file_name
        if not data:
            pass
        sheet = self.book.add_worksheet(sheet_name)
        if len(data) > 1:
            raise Exception('数据格式不正确')
        datainfo = data[0].get('info')
        for val in datainfo:
            col = start_col
            for row_content in val:
                content = row_content.get('content', '')
                cont_format = row_content.get('format', {})

                sheet.write(start_row, col, content, self.book.add_format(cont_format))
                if alignment:
                    curr_max_width = self.len_byte(content)
                    prev_max_width = col_width.get(colm[col], None)
                    if not prev_max_width:
                        col_width[colm[col]] = curr_max_width
                    if col_width.get(colm[col]) >= curr_max_width:
                        pass
                    else:
                        col_width[colm[col]] = curr_max_width
                    sheet.set_column('%s:%s' % (colm[col], colm[col]), col_width.get(colm[col]))
                col += 1
            start_row += 1
            col = start_col
        self.book.close()


x = TestWriteExcel()
x.write_excel(res)

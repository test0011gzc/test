# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""

res = {
    'file_name': '/aaa/bbb/yz.xlsx',
    'auto_span': True,
    'sheet_list': [
        {
            'sheet_name': 'sheet1',
            'data': [
                {
                    'start_row': 1,
                    'start_column': 1,
                    'info': [
                        [{'content': 'mch_id', 'format': {}}, {'content': 'bank_id', 'format': {}}],
                        [{'content': 'https://blog.csdn.net/qq_23387055/article/details/89706741', 'format': {}},
                         {'content': '1001', 'format': {}}]
                    ]
                },
                {
                    'start_row': 5,
                    'start_column': 4,
                    'info': [
                        [{'content': 'summary', 'format': {}}, {'content': 'total', 'format': {}},
                         {'content': 'fee_type', 'format': {}}],
                        [{'content': '2', 'format': {}}, {'content': '300', 'format': {}},
                         {'content': 'THB', 'format': {}}]
                    ]
                }
            ]
        },

        {
            'sheet_name': 'sheet2',
            'data': [
                {
                    'start_row': 3,
                    'start_column': 3,
                    'info': [
                        [{'content': 'mch_id', 'format': {'color': 'red',
                                                          'align': 'center', }}, {'content': 'bank_id', 'format': {}}],
                        [{'content': '20015', 'format': {}}, {'content': '1001', 'format': {}}]
                    ]
                },
                {
                    'start_row': 7,
                    'start_column': 1,
                    'info': [
                        [{'content': 'summary', 'format': {}}, {'content': 'total', 'format': {}},
                         {'content': 'fee_type', 'format': {}}],
                        [{'content': '2', 'format': {}},
                         {'content': 'https://blog.csdn.net/qq_23387055/article/details/89706741', 'format': {}},
                         {'content': 'THB', 'format': {'color': '#DDA0DD', }}]
                    ]
                }
            ]
        },
{
            'sheet_name': 'gzc',
            'data': [
                {
                    'start_row': 8,
                    'start_column': 10,
                    'info': [
                        [{'content': 'mch_id', 'format': {'color': 'red',
                                                          'align': 'center', }}, {'content': 'bank_id', 'format': {}}],
                        [{'content': '20015', 'format': {}}, {'content': '1001', 'format': {}}]
                    ]
                },
                {
                    'start_row': 7,
                    'start_column': 1,
                    'info': [
                        [{'content': 'summary', 'format': {}}, {'content': 'total', 'format': {}},
                         {'content': 'fee_type', 'format': {}}],
                        [{'content': '2', 'format': {}},
                         {'content': 'https://blog.csdn.net/qq_23387055/article/details/89706741', 'format': {}},
                         {'content': 'THB', 'format': {'color': '#DDA0DD', }}]
                    ]
                }
            ]
        }
    ]
}

import xlsxwriter as xw
import os
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
        file_name = res.get('file_name', 'test.xlsx')
        file_path = '/'.join(file_name.split('/')[:-1])
        if file_path:
            assert os.path.isdir(file_path) == True
        sheet_list = res.get('sheet_list', [])
        auto_span = res.get('auto_span', False)
        assert file_name.split('/',)
        self.book.filename = file_name
        for sheetdata in sheet_list:
            col_width = {}
            sheet_name = sheetdata.get('sheet_name', 'sheet1')
            sheet = self.book.add_worksheet(sheet_name)
            data = sheetdata.get('data', {})
            for datainfo in data:
                start_row = datainfo.get('start_row')
                start_column = datainfo.get('start_column')
                info = datainfo.get('info', {})
                if info:
                    for row in info:
                        st_col = start_column
                        for col in row:
                            content = col.get('content', '')
                            format = col.get('format', {})
                            sheet.write(start_row, st_col, content, self.book.add_format(format))
                            if auto_span:
                                curr_max_width = self.len_byte(content)
                                prev_max_width = col_width.get(colm[st_col], None)
                                if not prev_max_width:
                                    col_width[colm[st_col]] = curr_max_width
                                if col_width.get(colm[st_col]) >= curr_max_width:
                                    pass
                                else:
                                    col_width[colm[st_col]] = curr_max_width
                                sheet.set_column('%s:%s' % (colm[st_col], colm[st_col]), col_width.get(colm[st_col]))
                            st_col += 1
                        st_col = start_column
                        start_row += 1
        self.book.close()


x = TestWriteExcel()
x.write_excel(res)

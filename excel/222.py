# -*- coding: utf-8 -*-
"""
@Time    :
@Author  :  jalen
@Desc    :
"""

res = {
    'file_name': 'yz.xlsx',
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
import string
import xlsxwriter as xw
import os



class WriteExcel(object):

    def __init__(self):
        self.book = xw.Workbook()

    def calc_colm(self,index):
        '''
        :param index:
        :return: 索引对应的excel的列名
        '''
        #col = ABCDEFGHIJKLMNOPQRSTUVWXYZ
        col = string.ascii_uppercase
        col_list = []
        if index <= 25:
            col_name = col[index]
        else:
            for i in col[:index - 25]:
                for b in col[:index - 25]:
                    col_list.append(i + b)
            col_name = col_list[index - 26]
            del col_list
        return col_name

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
        :param res: res格式如下
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

        :return: 对应路径的excel文件
        '''
        file_name = res.get('file_name', 'test.xlsx')
        file_path = '/'.join(file_name.split('/')[:-1])
        if file_path:
            assert os.path.isdir(file_path) == True
        sheet_list = res.get('sheet_list', [])
        auto_span = res.get('auto_span', False)
        assert file_name.split('/', )
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
                                prev_max_width = col_width.get(self.calc_colm(st_col), None)
                                if not prev_max_width:
                                    col_width[self.calc_colm(st_col)] = curr_max_width
                                if col_width.get(self.calc_colm(st_col)) >= curr_max_width:
                                    pass
                                else:
                                    col_width[self.calc_colm(st_col)] = curr_max_width
                                sheet.set_column('%s:%s' % (self.calc_colm(st_col), self.calc_colm(st_col)), col_width.get(self.calc_colm(st_col)))
                            st_col += 1
                        st_col = start_column
                        start_row += 1
        self.book.close()


x = WriteExcel()
x.write_excel(res)







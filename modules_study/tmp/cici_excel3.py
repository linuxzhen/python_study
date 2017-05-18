#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
 Function: xlsxwrite画图
     Date: 2017/05/16
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""

import xlsxwriter
import random

class monthReport(object):
    def __init__(self, xls_file):
        self.workbook = xlsxwriter.Workbook(xls_file)
        self.worksheet = self.workbook.add_worksheet()
        self.bold = self.workbook.add_format({'bold': 1})
        self.format_subject = self.workbook.add_format({'bold': True, 'font_color': 'blue'})
        self.format_title = self.workbook.add_format({'bold': True, 'font_color': 'red'})
        self.format_text = self.workbook.add_format()

    # bar chart 条形
    # pie chart 饼
    # line chart 折线
    # column
    def get_num(self):
        return random.randrange(0, 100)

    def create_data(self):
        # 行成行列标题
        months = [u'', u'1月', u'2月', u'3月', u'4月', u'5月']
        parts = [u'A部门', u'B部门', u'C部门', u'D部门', u'E部门'],
        # 生成数据
        data = []
        for item in range(5):
            tmp = []
            for iitem in range(5):
                tmp.append(self.get_num())
            data.append(tmp)
        # 写入一行
        self.worksheet.set_column('A:A', 10, self.format_text)
        self.worksheet.write_row('A1', months, self.bold)
        # 写入一列
        self.worksheet.write_column('A2', data[0])
        self.worksheet.write_column('B2', data[1])
        self.worksheet.write_column('C2', data[2])
        self.worksheet.write_column('D2', data[3])

    def charts(self):
        # 创建一个图表，类型是column
        chart1 = self.workbook.add_chart({'type': 'column'})
        # 配置series,这个和前面worksheet是有关系的。
        #     指定图表的数据范围
        chart1.add_series({
            'name': '=Sheet1!$B$1',
            'categories': '=Sheet1!$A$2:$A$7',
            'values': '=Sheet1!$B$2:$B$7',
            'data_labels': {'value': True},
        })
        chart1.add_series({
            'name': "=Sheet1!$C$1",
            'categories': '=Sheet1!$A$2:$A$7',
            'values': '=Sheet1!$C$2:$C$7',
            'data_labels': {'value': True},
            'gap':150,
            'overlap': -50,
        })
        # 添加图表标题和标签
        chart1.set_title({'name': u'各部门支出数据'})
        chart1.set_x_axis({'name': 'Test number'})
        chart1.set_y_axis({'name': 'Sample length (mm)'})
    
        # 设置图表风格
        # chart1.set_style(2)
        chart1.set_size({'width': 720, 'height': 376})
        chart1.set_legend({'position': 'top'})
        chart1.set_y_axis({
            'major_gridlines': {
                'visible': False,
                'line': {'none': True}
            },
            'line': {'none': True},
            'num_font': {'color': '#FFFFFF'},
    
        })
        # 在D2单元格插入图表（带偏移）
        self.worksheet.insert_chart('A10', chart1, {'x_offset': 50, 'y_offset': 10})

    def close(self):
        self.workbook.close()

a = monthReport('a.xlsx')
a.create_data()
a.charts()
a.close()

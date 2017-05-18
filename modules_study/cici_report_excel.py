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

    def get_data(self):
        return random.randrange(0, 100)

    def create_data(self):
        # 行成行列标题
        months = [u'', u'1月', u'2月', u'3月', u'4月', u'5月']
        parts = [u'A部门', u'B部门', u'C部门', u'D部门', u'E部门']
        # 生成数据
        data = []
        for item in range(5):
            tmp = []
            for iitem in range(5):
                tmp.append(self.get_data())
            data.append(tmp)
        # 写入一行
        # self.worksheet.set_column('A:A', 10, self.format_text)
        self.worksheet.write_row('B1', months, self.bold)
        # 写入一列
        self.worksheet.write_column('B2', parts)
        self.worksheet.write_column('C2', data[0])
        self.worksheet.write_column('D2', data[1])
        self.worksheet.write_column('E2', data[2])
        self.worksheet.write_column('F2', data[3])
        self.worksheet.write_column('G2', data[4])

    def add_series(self, chart, name, categories, values):
        #  配置series
        #  指定图表的数据范围(一个列-图例)
        chart.add_series({
            'name': '='+name,             # 图例名
            'categories': '='+categories,  # 部门名
            'values': '='+values,      # 数据
            'data_labels': {'value': True},
        #    'gap':150,
        #    'overlap': -50,
        })
        
    def create_charts_column(self, location):
        # 创建一个图表，类型是column
        chart1 = self.workbook.add_chart({'type': 'column'})
        self.add_series(chart1, "Sheet1!$F$1", "Sheet1!$B$2:$B$6", "Sheet1!$F$2:$F$6")
        self.add_series(chart1, "Sheet1!$E$1", "Sheet1!$B$2:$B$6", "Sheet1!$C$2:$C$6")
        # 添加图表标题和标签
        chart1.set_title({'name': u'支出数据'})
        chart1.set_x_axis({'name': u'部门名称'})
        chart1.set_y_axis({'name': u'支出情况 (元)'})
        # 设置图表风格
        # chart1.set_style(2)
        chart1.set_size({'width': 500, 'height': 250})
        chart1.set_legend({'position': 'right'})
        # 插入图表(在location单元格)
        self.worksheet.insert_chart(location, chart1, {'x_offset': 0, 'y_offset': 0})

    def create_charts_line(self, location):
        # 创建一个图表，类型是line
        chart1 = self.workbook.add_chart({'type': 'line'})
        self.add_series(chart1, "Sheet1!$B$4", "Sheet1!$C$1:$G$1", "Sheet1!$C$4:$G$4")
        self.add_series(chart1, "Sheet1!$B$5", "Sheet1!$C$1:$G$1", "Sheet1!$C$5:$G$5")
        self.add_series(chart1, "Sheet1!$B$6", "Sheet1!$C$1:$G$1", "Sheet1!$C$6:$G$6")
        # 添加图表标题和标签
        chart1.set_title({'name': u'支出数据'})
        chart1.set_x_axis({'name': u'月份'})
        chart1.set_y_axis({'name': u'支出情况 (元)'})
        # 设置图表风格
        # chart1.set_style(2)
        chart1.set_size({'width': 500, 'height': 250})
        chart1.set_legend({'position': 'right'})
        # 插入图表(在location单元格)
        self.worksheet.insert_chart(location, chart1, {'x_offset': 0, 'y_offset': 0})

    def create_charts_pie(self, location):
        # 创建一个图表，类型是line
        chart1 = self.workbook.add_chart({'type': 'pie'})
        self.add_series(chart1, "Sheet1!$G$1", "Sheet1!$B$2:$B$6", "Sheet1!$G$2:$G$6")
        # 添加图表标题和标签
        chart1.set_title({'name': u'各部门支出'})
        chart1.set_x_axis({'name': u'部门名称'})
        chart1.set_y_axis({'name': u'支出情况 (元)'})
        # 设置图表风格
        # chart1.set_style(2)
        chart1.set_size({'width': 250, 'height': 250})
        chart1.set_legend({'position': 'right'})
        # 插入图表(在location单元格)
        self.worksheet.insert_chart(location, chart1, {'x_offset': 0, 'y_offset': 0})

    def create_charts_bar(self, location):
        # 创建一个图表，类型是bar
        chart1 = self.workbook.add_chart({'type': 'bar'})
        self.add_series(chart1, "Sheet1!$G$1", "Sheet1!$B$2:$B$6", "Sheet1!$G$2:$G$6")
        # 添加图表标题和标签
        chart1.set_title({'name': u'各部门支出'})
        chart1.set_x_axis({'name': u'支出情况 (元)'})
        # chart1.set_y_axis({'name': u'支出情况 (元)'})
        # 设置图表风格
        # chart1.set_style(2)
        chart1.set_size({'width': 250, 'height': 250})
        chart1.set_legend({'position': 'right'})
        # 插入图表(在location单元格)
        self.worksheet.insert_chart(location, chart1, {'x_offset': 0, 'y_offset': 0})

    def close(self):
        self.workbook.close()
def main(xls_file):
    xls_report = monthReport(xls_file)
    xls_report.create_data()
    xls_report.create_charts_line('B8')
    xls_report.create_charts_column('B21')
    xls_report.create_charts_pie('B34')
    xls_report.create_charts_bar('F34')
    xls_report.close()
    
if __name__ == "__main__":
    main('my_report.xlsx')

#!/usr/bin/env python
#-*- coding=utf-8 *-*
"""
 Function: xlsxwriter模块的使用
     Date: 2017/05/17
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""

import xlsxwriter
from datetime import datetime

def simple_file(xls_file):
    """创建一个简单的XLSX文件
    参  数：xls_file 文件名
    返回值: None
    """
    # 创建一个文件，并增加一个sheet
    workbook = xlsxwriter.Workbook(xls_file)
    worksheet = workbook.add_worksheet()
    # 定义即将写入的数据
    expenses = (
        ['Rent', 1000],
        ['Gas',   100],
        ['Food',  300],
        ['Gym',    50],
    )
    # 行和列下标从0开始写入数据
    row = 0
    col = 0
    # Iterate over the data and write it out row by row.
    for item, cost in (expenses):
        worksheet.write(row, col,     item)
        worksheet.write(row, col + 1, cost)
        row += 1
    # 向单元格写入Totol和SUM公式
    worksheet.write(row, 0, 'Total')
    worksheet.write(row, 1, '=SUM(B1:B4)')
    workbook.close()


def format_file(xls_file):
     # 创建一个文件，并增加一个sheet
     workbook = xlsxwriter.Workbook(xls_file)
     worksheet = workbook.add_worksheet()
     # 添加一个加粗格式
     bold = workbook.add_format({'bold': True})
     # 添加一个Money格式
     money = workbook.add_format({'num_format': '$#,##0'})
     # 写入表头（运用加粗格式）
     worksheet.write('A1', 'Item', bold)
     worksheet.write('B1', 'Cost', bold)
    # 定义即将写入的数据
     expenses = (
         ['Rent', 1000],
         ['Gas',   100],
         ['Food',  300],
         ['Gym',    50],
     )
     # 定义数据下标
     row = 1
     col = 0
     # 写入数据
     for item, cost in (expenses):
         worksheet.write(row, col,     item)
         worksheet.write(row, col + 1, cost, money)
         row += 1
    # 向单元格写入Totol和SUM公式,并分别设置格式
     worksheet.write(row, 0, 'Total',       bold)
     worksheet.write(row, 1, '=SUM(B2:B5)', money)

     workbook.close()

def different_file(xls_file):
    # 创建一个文件，并增加一个sheet
    workbook = xlsxwriter.Workbook(xls_file)
    worksheet = workbook.add_worksheet()
    # 新增bold、money和date格式
    bold = workbook.add_format({'bold': 1})
    money_format = workbook.add_format({'num_format': '$#,##0'})
    date_format = workbook.add_format({'num_format': 'mmmm d yyyy'})
    # 调整宽度
    worksheet.set_column(1, 1, 15)
    # 设置表头
    worksheet.write('A1', 'Item', bold)
    worksheet.write('B1', 'Date', bold)
    worksheet.write('C1', 'Cost', bold)
    # 定义数据
    expenses = (
        ['Rent', '2013-01-13', 1000],
        ['Gas',  '2013-01-14',  100],
        ['Food', '2013-01-16',  300],
        ['Gym',  '2013-01-20',   50],
    )
    # 定义写入位置开始下标
    row = 1
    col = 0
    # 写入数据
    for item, date_str, cost in (expenses):
        # 转换格式
        date = datetime.strptime(date_str, "%Y-%m-%d")
        worksheet.write_string  (row, col,     item              )
        worksheet.write_datetime(row, col + 1, date, date_format )
        worksheet.write_number  (row, col + 2, cost, money_format)
        row += 1
    worksheet.write(row, 0, 'Total', bold)
    worksheet.write(row, 2, '=SUM(C2:C5)', money_format)
    workbook.close()

def chart_file():
    workbook = xlsxwriter.Workbook('chart.xlsx')
    worksheet = workbook.add_worksheet()
    # Create a new Chart object.
    chart = workbook.add_chart({'type': 'column'})
    # Write some data to add to plot on the chart.
    data = [
        [1, 2, 3, 4, 5],
        [2, 4, 6, 8, 10],
        [3, 6, 9, 12, 15],
    ]
    worksheet.write_column('A1', data[0])
    worksheet.write_column('B1', data[1])
    worksheet.write_column('C1', data[2])
    # Configure the chart. In simplest case we add one or more data series.
    chart.add_series({'values': '=Sheet1!$A$1:$A$5'})
    chart.add_series({'values': '=Sheet1!$B$1:$B$5'})
    chart.add_series({'values': '=Sheet1!$C$1:$C$5'})
    # Insert the chart into the worksheet.
    worksheet.insert_chart('A7', chart)
    workbook.close()

if __name__ == "__main__":
    simple_file("simple_file.xlsx")
    format_file("format_file.xlsx")
    different_file("different_file.xlsx")
    chart_file()

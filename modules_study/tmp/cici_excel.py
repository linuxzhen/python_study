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

def charts():
    workbook = xlsxwriter.Workbook('chart_column.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})

    # 这是个数据table的列
    headings = ['Number', 'Batch 1', 'Batch 2', 'Batch 3']
    data = [
    ['aabbb-\ndasfdadf', 'fdajdad-\ngddfddfefafdsgf', 'dadafd-\neefeffdsafd', 'jfeiofij-fjdjfd', 'jdojf-ddjfdad', 'dfjaod-dafd'],
        [10, 40, 50, 20, 10, 50],
        [30, 60, 70, 50, 40, 30],
        [1,2,3,4,5,6]
    ]
    # 写入一行

    format = workbook.add_format()
    format.set_text_wrap()
    worksheet.set_column('A:A', 10, format)

    worksheet.write_row('A1', headings, bold)
    # 写入一列
    worksheet.write_column('A2', data[0])
    worksheet.write_column('B2', data[1])
    worksheet.write_column('C2', data[2])
    worksheet.write_column('D2', data[3])
    ############################################
    # 创建一个图表，类型是column
    chart1 = workbook.add_chart({'type': 'column'})
    line_chart = workbook.add_chart({'type': 'line'})

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
    line_chart.add_series({
        'name': "=Sheet1!$D$1",
        'categories': '=Sheet1$A2:$A$7',
        'values': '=Sheet1!$D2$2:$D$7',
        'data_label':{'value': True},
    })
    # 添加图表标题和标签
    chart1.set_title({'name': u'中文Results of sample analysis'})
    chart1.set_x_axis({'name': 'Test number'})
    #chart1.set_y_axis({'name': 'Sample length (mm)'})

    # 设置图表风格
    #chart1.set_style(2)
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
    #chart1.combine(line_chart)
    worksheet.insert_chart('D3', chart1, {'x_offset': 50, 'y_offset': 10})
    workbook.close()

charts()

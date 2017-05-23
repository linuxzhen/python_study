#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
 Function: 用传统的方法来统计数据
     Date: 2017/05/23
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""
file="./pd.data"
data_count = {}
with open(file, 'r') as f:
    for eachline in f:
        if eachline in data_count.keys():
            data_count[eachline] += 1
        else:
            data_count[eachline] = 0
print data_count

#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
 Function: 检查IP是否允许登录
     Date: 2017/05/15
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""

from IPy import IP

WHITE_HOST = ['192.168.0.1/32',
              '192.168.137.0/24']

def is_sub_net(ipaddress, net, mask):
    """判断ipaddress是不是属于net的子网
    参  数：ipaddress, string, IP地址
            net, string, 子网
            mask, string/int, 掩码位
    返回值：Boole, True/False
    """
    net = IP(net).make_net(mask)
    if ipaddress in IP(net):
        return True
    return False

def check_validity(ipaddress):
    """判断ipaddress是不是合法
    参  数：ipaddress, string, IP地址
    返回值：Boole, True/False
    """
    for item in WHITE_HOST:
        acl_ip = item.split('/')[0]
        acl_net = item.split('/')[1]
        if(is_sub_net(ipaddress, acl_ip, acl_net)):
            return True
    return False

if __name__ == "__main__":
    ip = raw_input("请输入一个IP:")
    if check_validity(ip):
        print("IP 合法")
    else:
        print("IP 不合法")

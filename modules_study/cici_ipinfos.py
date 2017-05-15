#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
 Function: 根据输入的IP或子网返回网段、掩码、广播、反向解析、子网数、IP类型等
     Date: 2017/05/14
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""

from IPy import IP

def net_infos():
    ip = raw_input("请输入一个IP或网段:")
    ips = IP(ip)
    if len(ips) > 1:
        print("网段:%s" % ips.net())
        print("子网掩码:%s" % ips.netmask())
        print("广播地址:%s" % ips.broadcast())
        print("反向解析:%s" % ips.reverseNames()[0])
        print("子网数:%s" % len(ips))
    else:
        print "反向解析:%s" % ips.reverseName()[0]
        print "十六进制:%s" % ips.strHex()
        print "二进制:%s" % ips.strBin()
        print "IP类型:%s" % ips.iptype()

if __name__ == "__main__":
    net_infos()

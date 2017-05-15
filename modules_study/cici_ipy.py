#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
 Function: IPy模块学习
     Date: 2017/05/14
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""

from IPy import IP, IPSet

def help():
    """
    psutil is a cross-platform library for retrieving information on
running processes and system utilization (CPU, memory, disks, network)
in Python.
    Psutil 是一个跨平台库。能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。
    它主要应用于系统监控，分析和限制系统资源及进程的管理。
    它实现了同等命令行工具提供的功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、free、
    nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。
    """
    return 0


if __name__ == "__main__":
    # 通过指定的网段输出该网段的IP个数及所有IP地址清单
    ip0 = IP('192.168.137.0/30')
    for item in ip0:
        print(item)

    # 输出IP是哪类IPv4 或 IPv6
    ip1 = "192.168.137.1"
    ip2 = "::1"
    print(IP(ip1).version())
    print(IP(ip2).version())
    
# 反向解析名称、IP类型、IP转换
ip = IP("192.168.1.20")
print(ip.reverseName())
print(ip.iptype())
print(IP("8.8.8.8").int())

# 网络地址转换
print (IP("192.168.1.0").make_net("255.255.255.0"))

# 将网络地址转化为友好的方式
print(IP('10.0.0.0/32').strNormal())
print(IP('10.0.0.0/24').strNormal())
print(IP('10.0.0.0/24').strNormal(0))
print(IP('10.0.0.0/24').strNormal(1))
print(IP('10.0.0.0/24').strNormal(2))
print(IP('10.0.0.0/24').strNormal(3))

# 网络计算
print(IP("10.0.0.0/24") < IP("12.0.0.0/24"))
print("192.168.1.100" in IP("192.168.1.0/24"))

# 判断两个网段是否存在重叠
print(IP("192.168.0.0/23").overlaps("192.168.1.0/24"))



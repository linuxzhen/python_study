#!/usr/bin/env python
"""
@author: cici
@date:   20170512
@function:
    Psutil模块学习
@changelog:
    v0.1 init
"""
import Psutil
import psutil

def help():
    """
    Psutil is a cross-platform library for retrieving information on
running processes and system utilization (CPU, memory, disks, network)
in Python.
    Psutil 是一个跨平台库。能够轻松实现获取系统运行的进程和系统利用率（包括CPU、内存、磁盘、网络等）信息。
    它主要应用于系统监控，分析和限制系统资源及进程的管理。
    它实现了同等命令行工具提供的功能，如ps、top、lsof、netstat、ifconfig、who、df、kill、free、
    nice、ionice、iostat、iotop、uptime、pidof、tty、taskset、pmap等。
    """
    return 0

def hd_cpu():
    """返回CPU硬件信息
    Args：无
    Returns: 0
    """

    # 显示cpu的整个信息
    print(psutil.cpu_times())

    # 获取单项值, 如果要只但看那个的话就在后边加上.xxx就行了
    print(psutil.cpu_times().user)
    print(psutil.cpu_times()[0])

    # 获取cpu的逻辑个数
    print(psutil.cpu_count())

    # 获取cpu的物理个数
    print(psutil.cpu_count(logical=False))

    return 0



if __name__ == "__main__":
    hd_cpu()


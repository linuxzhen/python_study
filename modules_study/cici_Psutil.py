#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
@author: cici
@date:   20170512
@function:
    Psutil模块学习
@changelog:
    v0.1 init
"""

import psutil

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

def hd_cpu():
    """返回CPU硬件信息
    参  数：无
    返回值: 返回一个字典
        cpu_logic_nums: 逻辑cpu个数
        cpu_hd_nums: 物理cpu个数
    """

    # cpu的逻辑个数
    cpu_logic_nums = psutil.cpu_count()
    # cpu的物理个数
    cpu_hd_nums = psutil.cpu_count(logical=False)

    hd_cpu_dic = {
        "cpu_logic_nums": cpu_logic_nums,
        "cpu_hd_nums": cpu_hd_nums
    }
    print("cpu个数:{hd_cpu_dic}".format(hd_cpu_dic=hd_cpu_dic))
    return hd_cpu_dic


def sys_cpu():
    """返回CPU使用信息
    参  数：无
    返回值: 返回一个字典
        cpu_user: 用户使用时间，
        cpu_sys: 系统使用时间,
        cpu_idle: 空闲时间,
        cpu_interrupt: 硬件中断时间,
        cpu_dpc: 延迟过程调用时间,
    """

    # cpu的整个信息
    cpu_all = psutil.cpu_times()
    # 获取单项值, 如果要只但看那个的话就在后边加上.xxx就行了
    cpu_user = psutil.cpu_times().user
    cpu_sys = psutil.cpu_times()[1]
    cpu_idle = psutil.cpu_times()[2]
    cpu_interrupt = psutil.cpu_times()[3]
    cpu_dpc = psutil.cpu_times()[4]
    sys_cpu_dic = {
        "cpu_user": cpu_user,
        "cpu_sys": cpu_sys,
        "cpu_idle": cpu_idle,
        "cpu_interrupt": cpu_interrupt,
        "cpu_dpc": cpu_dpc,
    }
    print("cpu的整个信息:{cpu_all}".format(cpu_all=cpu_all))
    print("cpu的使用时间分布:{sys_cpu_dic}".format(sys_cpu_dic=sys_cpu_dic))
    return sys_cpu_dic

def sys_mem():
    """返回内存使用信息
    参  数：无
    返回值: 返回一个字典
        "sys_mem_total": sys_mem_total,
        "sys_mem_available": sys_mem_available,
        "sys_mem_percent": sys_mem_percent,
        "sys_mem_used": sys_mem_used,
        "sys_mem_free": sys_mem_free,
        "sys_mem_swap_total": sys_mem_swap_total
    """

    sys_mem_all = psutil.virtual_memory()
    sys_mem_total = sys_mem_all.total
    sys_mem_available = sys_mem_all.available
    sys_mem_percent = sys_mem_available / sys_mem_total
    sys_mem_used = sys_mem_all.used
    sys_mem_free = sys_mem_all.free

    sys_mem_dic = {
        "sys_mem_total": sys_mem_total,
        "sys_mem_available": sys_mem_available,
        "sys_mem_percent": sys_mem_percent,
        "sys_mem_used": sys_mem_used,
        "sys_mem_free": sys_mem_free,
        "sys_mem_swap_total": sys_mem_swap_total
    }
    print(sys_mem_total)
    print(sys_cpu_dic)
    return sys_mem_dic

def sys_swap():
    sys_mem_swap_all = psutil.swap_memory()
    sys_mem_swap_total = sys_mem_swap_all.total
    sys_mem_swap_used = sys_mem_swap_all.used
    sys_mem_swap_free = sys_mem_swap_all.free
    sys_mem_swap_percent = sys_mem_swap_all.percent
    sys_mem_swap_sin = sys_mem_swap_all.sin
    sys_mem_swap_sout = sys_mem_swap_all.sout

if __name__ == "__main__":
    hd_cpu()
    sys_cpu()
    sys_mem()
    sys_swap()


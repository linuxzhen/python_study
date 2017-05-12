#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
 Function: Psutil模块学习
     Date: 2017/05/12
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
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
    print("cpu个数:\n\t{hd_cpu_dic}".format(hd_cpu_dic=hd_cpu_dic))
    return hd_cpu_dic

def sys_cpu():
    """返回CPU使用信息(注意Win和Linux输出的内容会有些差异)
    参  数：无
    返回值: 返回一个scputimes类
        scputimes(user=71.57, nice=0.04, system=140.89, idle=201280.93, iowait=25.84, irq=0.0, softirq=12.85, steal=0.0, guest=0.0, guest_nice=0.0)
        获取单项值, 加上.xxx或加序号就可以获取到
        psutil.cpu_times().user
        psutil.cpu_times()[1]
    """

    # cpu的整个信息
    cpu_all = psutil.cpu_times()
    print("cpu使用:\n\t{cpu_all}".format(cpu_all=cpu_all))
    return cpu_all

def sys_mem():
    """返回内存使用信息
    参  数：无
    返回值: 返回一个svmem类
        svmem(total=1032622080, available=656125952, percent=36.5, used=202153984, free=190681088, active=335327232, inactive=336580608, buffers=77824, cached=639709184, shared=13565952)
        获取单项值, 加上.xxx或加序号就可以获取到
    """

    sys_mem_all = psutil.virtual_memory()
    print("物理内存使用:\n\t{sys_mem_all}".format(sys_mem_all=sys_mem_all))
    return sys_mem_all

def sys_swap():
    """返回swap使用信息
    参  数：无
    返回值: 返回一个sswap类
        sswap(total=2147479552, used=0, free=2147479552, percent=0.0, sin=0, sout=0)
        获取单项值, 加上.xxx或加序号就可以获取到
    """

    sys_swap_all = psutil.swap_memory()
    print("swap使用:\n\t{sys_swap_all}".format(sys_swap_all=sys_swap_all))
    return sys_swap_all

def sys_diskio():
    """返回磁盘IO使用信息
    参  数：无
    返回值: 返回一个sdiskio类
        sdiskio(read_count=15567, write_count=45528, read_bytes=461906432, write_bytes=1571985408, read_time=18795, write_time=375514, read_merged_count=11, write_merged_count=3899, busy_time=65020)
        获取单项值, 加上.xxx或加序号就可以获取到
    """

    sys_diskio_all = psutil.disk_io_counters()
    # perdisk=True参数获取单个分区IO个数
    # sys_diskio_per_all = psutil.disk_io_counters(perdisk=True)    
    print("diskio使用:\n\t{sys_diskio_all}".format(sys_diskio_all=sys_diskio_all))
    return sys_diskio_all

def sys_netio():
    """返回网络IO信息
    参  数：无
    返回值: 返回一个字典，包括每个网卡的信息，每个网卡的信息是一个snetio类
        {'lo': snetio(bytes_sent=0, bytes_recv=0, packets_sent=0, packets_recv=0, errin=0, errout=0, dropin=0, dropout=0), 'ens33': snetio(bytes_sent=5613402, bytes_recv=95532504, packets_sent=46461, packets_recv=113839, errin=0, errout=0, dropin=0, dropout=0)}
        获取单项值, 加上.xxx或加序号就可以获取到
    """

    # sys_netio_all = psutil.net_io_counters()
    # pernic=True输出网络每个接口信息
    sys_netio_all = psutil.net_io_counters(pernic=True)
    print("网络IO使用:\n\t{sys_netio_all}".format(sys_netio_all=sys_netio_all))
    return sys_netio_all

def sys_disk_partition():
    """返回磁盘分区信息
    参  数：无
    返回值: 返回一个列表，包括每个分区的信息，每个分区的信息是一个sdiskpart类
        [sdiskpart(device='/dev/mapper/cl-root', mountpoint='/', fstype='xfs', opts='rw,seclabel,relatime,attr2,inode64,noquota'), sdiskpart(device='/dev/sda1', mountpoint='/boot', fstype='xfs', opts='rw,seclabel,relatime,attr2,inode64,noquota')]
        获取单项值, 加上.xxx或加序号就可以获取到
    """

    sys_disk_partition_all = psutil.disk_partitions()
    print("磁盘分区分区信息:\n\t{sys_disk_partition_all}".format(
        sys_disk_partition_all=sys_disk_partition_all))
    return sys_disk_partition_all


def sys_disk_usage(part):
    """返回磁盘分区容量信息
    参  数：分区名,str
    返回值: 返回一个sdiskusage类
        sdiskusage(total=18238930944, used=1444638720, free=16794292224, percent=7.9)
        获取单项值, 加上.xxx或加序号就可以获取到
    """

    sys_disk_partition_all = psutil.disk_partitions
    sys_disk_usage_all = psutil.disk_usage(part)
    print("磁盘分区容量信息:\n\t{sys_disk_usage_all}".format(
        sys_disk_usage_all=sys_disk_usage_all))
    return sys_disk_usage_all

def sys_user():
    """返回当前登录用户信息
    参  数：无
    返回值: 返回一个列表，包括当前登录的所有用户，每个用户的信息是一个suser类
        获取单项值, 加上.xxx或加序号就可以获取到
    """
    sys_user_all = psutil.users()
    print("当前登录用户信息:\n\t{sys_user_all}".format(sys_user_all=sys_user_all))
    return sys_user_all

def sys_pids():
    # 查看系统全部进程
    sys_pids_all = psutil.pids()
    print(sys_pids_all)

def sys_proc(pid):
    # 使用psutil.Process()方法获取单个进程的名称,路径状态等
    sys_proc_all = psutil.Process(pid)
    print("指定PID的信息：{sys_proc_all}".format(sys_proc_all=sys_proc_all))
    # sys_proc_all.pid

if __name__ == "__main__":
    hd_cpu()
    sys_cpu()
    sys_mem()
    sys_swap()
    sys_diskio()
    sys_disk_partition()
    sys_disk_usage('/')
    sys_netio()
    sys_user()
    sys_pids()
    sys_proc(1)

#!/usr/bin/env python
#-*- coding=utf-8 *-*
"""
 Function: 网络流量监控
     Date: 2017/05/14
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""

import json
import psutil
from cici_get_size_in_nice_string import get_size_in_nice_string


def sys_net(pernic=False):
    """返回网卡流量信息
    参  数：pernic, Bool, 是否取各个网卡（True则分别取不同网卡）
    返回值: 返回一个字典
            {"ret_info": {"recv": "1.85 MB", "sent": "1.32 MB"}, "ret_code": 0}
            {"ret_info": {"lo": {"recv": "27.23 KB", "sent": "27.23 KB"}, "ens33": {"recv": "1.91 MB", "sent": "1.41 MB"}}, "ret_code": 0}
    """
    ret = {}
    ret["ret_code"] = 0
    try:
        net_io = psutil.net_io_counters(pernic=pernic)
        if pernic:
            ret["ret_info"] = {}
            each_nic = {}
            for item_net_io in net_io:
                net_sent = get_size_in_nice_string(net_io[item_net_io].bytes_sent)
                net_recv = get_size_in_nice_string(net_io[item_net_io].bytes_recv)
                each_nic = {"sent":net_sent, "recv": net_recv}
                ret["ret_info"][item_net_io] = each_nic
        else:
            net_sent = get_size_in_nice_string(net_io.bytes_sent)
            net_recv = get_size_in_nice_string(net_io.bytes_recv)
            ret["ret_info"] = {"sent":net_sent, "recv": net_recv}
    except Exception as ex:
        ret["ret_code"] = -1
        ret["ret_info"] = ex
    return json.dumps(ret)

if __name__ == "__main__":
    print(sys_net(True))

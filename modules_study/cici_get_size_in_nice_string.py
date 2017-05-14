#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
 Function: 将大小转换为最佳单位
     Date: 2017/05/14
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""

def get_size_in_nice_string(size_in_bytes):
    """将bytes大小转换为最佳单位(KB、MB、GB、TB)
    参  数：size_in_bytes, 单位为bytes的大小
    返回值: 返回一个字符串，形如 97.7 KB
    """
    for (base_size, label) in [(1024*1024*1024*1024, "TB"),
                            (1024*1024*1024, "GB"),
                            (1024*1024, "MB"),
                            (1024, "KB"),
                            (1, "B"),
                            ]:
        if size_in_bytes >= base_size:
            return "{size:.2f} {label}".format(size=size_in_bytes * 1.0 / base_size, label=label)
    if size_in_bytes == 1:
        return "1 byte"
    else:
        bytes = "{size_in_bytes:.2f}".format(size_in_bytes=size_in_bytes)
        return (bytes[:-2] if bytes.endswith('.0') else bytes) + ' bytes'

if __name__ == "__main__":
    print(get_size_in_nice_string(100004))

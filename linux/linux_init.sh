#!/bin/bash

sed -i '/^GATEWAY/d' /etc/sysconfig/network
echo "GATEWAY=192.168.80.1" >> /etc/sysconfig/network
sed -i '/^nameserver/d' /etc/resolv.conf
echo "nameserver 192.168.80.1" >> /etc/resolv.conf
/etc/init.d/network restart
cd /etc/yum.repos.d/;
curl http://mirrors.163.com/.help/CentOS7-Base-163.repo > CentOS7-Base-163.repo
yum install vim wget -y
hostname $1
echo $1 > /etc/hostname

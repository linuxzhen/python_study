#!/usr/bin/env python
#-*— coding=utf-8 *-*
"""
 Function: 创建一个发邮件的类
     Date: 2017/05/15
   Author: cici
    Email: linuxzhen520@163.com
Changelog: v0.1 init
"""

from mailer import Mailer
from mailer import Message

class ciciMailer(object):
    def __init__(self,
                 host='mail.qq.com',
                 port=25,
                 sender='3267358568@qq.com',
                 pwd='pjbh1264'):
        self.host = host
        self.port = port
        self.sender = sender
        self.pwd = pwd

    def send(self, receiver, subject, body):
        message = Message(From=self.sender, To=receiver, charset="utf-8")
        message.Subject = subject
        message.Html = "<h1>xxx</h1>"
        message.Body = "xxxx"
        #message.attach("cici_check_ip_validity.py")
        sender = Mailer(host=self.host, pwd=self.pwd, usr=self.sender)
        sender.send(message)

mail = ciciMailer()
mail.send(receiver="linuxzhen520@163.com", subject="test email", body="RT")

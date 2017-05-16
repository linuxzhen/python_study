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
                 host='smtp.163.com',
                 port=465,
                 sender='linuxzhen520@163.com',
                 pwd='JLBIR77J'):
        self.host = host
        self.port = port
        self.sender = sender
        self.pwd = pwd

    def send(self, receiver, subject, body, attach=None):
        message = Message(From=self.sender, To=receiver, charset="utf-8")
        message.Subject = subject
        # Html or Body
        message.Html = body
        # message.Body = body
        if attach:
            message.attach(attach)
        try:
            sender = Mailer(host=self.host, pwd=self.pwd, usr=self.sender, use_ssl=True)
            sender.send(message)
        except Exception as ex:
            print(ex)
            return False
        return True

if __name__ == "__main__":
    mail = ciciMailer()
    #mail = ciciMailer(host='smtp.qq.com',
    #                  port=465,
    #                  sender='954365910@qq.com',
    #                  pwd='bujubcztpsvbbfdf')
    if(mail.send(receiver="linuxzhen520@163.com", subject="test email", body="<h1>xxx</h1>", attach="/tmp/a.sh")):
        print("邮件发送成功!")

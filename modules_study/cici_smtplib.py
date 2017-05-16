#! /usr/bin/env python  
# -*- coding: UTF-8 -*-  
import smtplib  
from email.mime.text import MIMEText  

# 使用的邮箱的smtp服务器地址，这里是163的smtp地址  
mail_host="smtp.163.com"
# 用户名  
mail_user="linuxzhen520"
# 授权码 
mail_pass="JLBIR77J"
# 邮箱的后缀，网易就是163.com 
mail_postfix="163.com"

def send_mail(receiver, subject, content):  
    me="hello"+"<"+mail_user+"@"+mail_postfix+">"  
    msg = MIMEText(content,_subtype='plain')  
    msg['Subject'] = subject
    msg['From'] = me  
    # 将收件人列表以‘；’分隔  
    msg['To'] = ";".join(receiver)
    try:  
        server = smtplib.SMTP()
        # 连接服务器  
        server.connect(mail_host)
        # 登录操作  
        server.login(mail_user,mail_pass)
        server.sendmail(me, receiver, msg.as_string())  
        server.close()  
        return True  
    except Exception, e:  
        print(str(e)) 
        return False  

mail_receiver=['linuxzhen520@163.com']           #收件人(列表)  
if send_mail(mail_receiver,'test','testxxxx'):
    print("邮件发送成功!")

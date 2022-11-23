#!/usr/bin/python3
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.header import Header
 
# 第三方 SMTP 服务
mail_host="smtp.163.com"  #设置服务器
mail_user="sys__warning"    #用户名
mail_pass="Syswarning__123"   #口令 
sender = 'sys__warning@163.com'
receivers = ['3040207@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
   

def sendemail(title,content):
    
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("系统提示邮件", 'utf-8')
    message['To'] =  Header("no reply", 'utf-8')    
    subject = 'Python SMTP 邮件测试'
    if len(title)>0:
        subject=title

    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP() 
        smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
        smtpObj.login(mail_user,mail_pass)  
        smtpObj.sendmail(sender, receivers, message.as_string())
        print ("邮件发送成功")
    except smtplib.SMTPException:
        print ("Error: 无法发送邮件")
    return

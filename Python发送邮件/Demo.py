# -*- coding:UTF-8 -*-

__author__ = 'gancj'

__data__ = '2015-06-19 22:17'

__mail__ = 'gancj@ucweb.com/393037282@qq.com'


#coding: utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'ucwebautotest@163.com'
receiver = '393037282@qq.com'

subject = 'python email test'
smtpserver = 'smtp.163.com'
username = 'ucwebautotest@163.com'
password = 'ucwebautotest123'

msg = MIMEText('你好','text','utf-8')#中文需参数‘utf-8’，单字节字符不需要
msg['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()
smtp.connect('smtp.163.com')
smtp.login(username, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
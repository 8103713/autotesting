#coding=gbk
# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
import random
from email.mime.multipart import MIMEMultipart
import smtplib
import datetime
import os,sys,time
import ConfigParser



class SendEmail(object):
    def __init__(self,smtpserver,username,password,reciver_list,subject,body):
        self.smtpserver = smtpserver
        self.username = username
        self.password = password
        self.reciver_list = reciver_list
        self.body = body
        self.subject = subject

    '''发送邮件'''
    def send_email(self, msg,type=None):
        try:
            if not type:
                smtp = smtplib.SMTP()
                smtp.connect(self.smtpserver,25)
                smtp.login(self.username, self.password)
                smtp.sendmail(self.username, self.reciver_list, msg.as_string())
                smtp.quit()
                print "sending!!"
            else:
                smtp = smtplib.SMTP_SSL(smtpserver, 465)
                smtp.login(self.username, self.password)
                smtp.sendmail(self.username, self.reciver_list, msg.as_string())
                smtp.quit()
                print "sending!!"
        except Exception, e:
            print str(e)
            print "sending fail"

    #附件邮件，构造附件,attachment_path_file_list有内容则发送附件，为空则只发送文本
    def attachment(self, attachment_files=None):
        msg = MIMEMultipart()
        msg['Subject'] = self.subject
        msg['From'] = self.username
        msg['to'] = ";".join(self.reciver_list)
        body = MIMEText(self.body, _subtype='plain', _charset='gb2312')
        msg.attach(body)
        atts = []
        try:
            i = 0
            for attachment_file in attachment_files:
                att = MIMEText(open(attachment_file, 'rb').read(), 'base64', 'gb2312')
                att["Content-Type"] = 'application/octet-stream'
                att["Content-Disposition"] = 'attachment; filename=%s' % attachment_file.split("\\")[-1]
                atts.append(att)
                msg.attach(atts[i])
                i += 1
            return msg
        except:
            return msg


if __name__ == "__main__":
    site = sys.argv[1]
    files = sys.argv[2]
    time.sleep(2)
    path = "..\\results\\%s\\" % site
    cf = ConfigParser.RawConfigParser()
    cf.read("smtplib.ini")
    username = cf.get("configuration", "username")
    password = cf.get("configuration", "password")
    smtpserver = cf.get("configuration", "smtpserver")
    mailto_listtmp = cf.get("configuration", "mailto_list")
    mailto_list = mailto_listtmp.split(",")
    body = "你好，\n这里是一封自动化测试结果汇报邮件\n请查收"
    attachment_files = []
    for i in files.split(","):
        attachment_files.append(path + i)
    print attachment_files
    test_subject = '自动化结果反馈'
    sendemail = SendEmail(smtpserver,username,password,mailto_list,test_subject,body)
    text = sendemail.attachment(attachment_files)
    sendemail.send_email(text,"1")

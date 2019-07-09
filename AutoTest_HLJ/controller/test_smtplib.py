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

    '''�����ʼ�'''
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

    #�����ʼ������츽��,attachment_path_file_list���������͸�����Ϊ����ֻ�����ı�
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
    body = "��ã�\n������һ���Զ������Խ���㱨�ʼ�\n�����"
    attachment_files = []
    for i in files.split(","):
        attachment_files.append(path + i)
    print attachment_files
    test_subject = '�Զ����������'
    sendemail = SendEmail(smtpserver,username,password,mailto_list,test_subject,body)
    text = sendemail.attachment(attachment_files)
    sendemail.send_email(text,"1")

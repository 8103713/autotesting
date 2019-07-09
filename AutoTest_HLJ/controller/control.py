#coding=gbk
# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-

import unittest
from controller import HTMLTestRunnerCN
import datetime
import os
import logging

def control(site,all_cases,title,tester):
    cases = ''
    for i in all_cases.split(","):
        cases += "testcases.%s.case.%s," % (site,i)
    tarformate = cases[:-1].split(",")
    print (tarformate)

    FloderName = current_time("%Y%m%d_%H%M%S")

    suite = unittest.TestLoader().loadTestsFromNames(tarformate)

    src = site + os.sep + FloderName
    checkEnvir("..\\..\\results\\%s" % site)
    #生成html的测试报告
    filename = "..\\..\\results\\" + src + "_result.html"
    ft = open(filename, "wb")
    runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream =ft,
        title = title,
        tester = tester
                                        )
    runner.run(suite)
    ft.close()

    #将测试结果打包

"""
site = sys.argv[1]
allcases = sys.argv[2]

#testcase.heilognjiang.test_1000_putongkaihu
cases = ''
for i in allcases.split(","):
    cases += "testcases.%s.case.%s," % (site,i)


tarformate = cases[:-1].split(",")
print (tarformate)
"""

def ChosePath():
    env_dist = os.environ
    lists = env_dist.get("path").split(";")
    path = ''
    for i in lists:
        if 'python' in i or 'Python' in i:
            if 'script' not in i or 'Script' not in i:
                path = i
    currentpathlist = os.getcwd().split("\\")
    if "testcases" in currentpathlist:
        tarindex = currentpathlist.index("testcases")
    if "public" in currentpathlist:
        tarindex = currentpathlist.index("public")
    if "controller" in currentpathlist:
        tarindex = currentpathlist.index("controller")
    tarfile = currentpathlist[tarindex - 1] + ".pth"
    tarpath = path + os.sep + "Lib" + os.sep + "site-packages" + os.sep + tarfile
    with open(tarpath) as f:
        lines = f.readlines()
    return lines[0] + os.sep


def log():
    tarpath = ChosePath()
    logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='%slog\\controler.log' % tarpath,filemode='a')


#格式化当前日期[%Y%m%d-%H%M%S]
def current_time(format):
    now = datetime.datetime.now()
    recice_time = now.strftime("%s" % format)
    return recice_time


def checkEnvir(tar):
    if os.path.exists(tar):
        pass
    else:
        os.mkdir(tar)
"""
FloderName = current_time("%Y%m%d_%H%M%S")


suite = unittest.TestLoader().loadTestsFromNames(tarformate)


src = site + os.sep + FloderName
checkEnvir("..\\results\\%s" % site)
#生成html的测试报告
filename = "..\\results\\" + src + "_result.html"
ft = open(filename, "wb")
runner = HTMLTestRunner.HTMLTestRunner(
      stream =ft,
      title = "Inspection case",
      description = "Inspection case"
                                        )
runner.run(suite)
ft.close()

#将测试结果打包
os.system("python package.py %s %s" % (site,FloderName))
"""
'''
#发送邮件
os.system("python test_smtplib.py %s %s.zip" % (site,FloderName))
'''


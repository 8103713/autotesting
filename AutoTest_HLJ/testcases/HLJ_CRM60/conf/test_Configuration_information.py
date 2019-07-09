__author__ = 'liuss'
# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-

import os
from public import test_UIbase

path = test_UIbase.ChosePath()

#定义项目名称
site = "HLJ_CRM60"

#定义浏览器
platform = "Chrome"

#定义日志路径级别
class LogConfig:
    loglevel = "debug"
    path = path + "log\\"
    name = "%s.log" % site
    logpath = '%s%s' %(path,name)
    Log =  test_UIbase.logconfig(logpath,loglevel)

#定义URL
class UrlConfig:
    #初始地址
    base_url = "http://10.149.85.39:46000/eppage/login.html"

#定义地市代码
class CityConfig:
    city_code="2301"

#定义校验点定位标识
class checkTag:
    #输入opcode步骤验证是否正确跳转功能页面
    #定位：导航div标签的id属性
    QuickSearch="2000072261"

#定义一些列举值列表的顺序
class IndexConfig:
    #证件类型
    id_types=["01","02","05","06","07","31","18","20","08","09","10","11","30","33"]

class ScreenShot:
    ScreenShotPath = path + "results\\" + site + os.sep
"""
class SleepTime:
    #Waiting time between the operation steps
    StepSleepTime = 0.5
    #Wait operation response time
    ResponseSleepTime = 3
    #Positioning element waiting time
    LocalSleepTime = 1
"""
def userName(city_code):
    if(city_code=='2301'):
        return "aheb05"
def userPwd(city_code):
    if(city_code=='2301'):
        return "111111"
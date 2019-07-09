__author__ = 'liuss'
# -*- coding: cp936 -*-
# -*- coding: utf-8 -*-

import os
from public import test_UIbase

path = test_UIbase.ChosePath()

#定义项目名称
site = "demo"

#定义浏览器
platform = "firefox"

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
    baseurl = "http://www.baidu.com/"

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
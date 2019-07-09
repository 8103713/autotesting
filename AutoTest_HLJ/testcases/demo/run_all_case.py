__author__ = 'liuss'

#coding:utf-8

from controller import control
from testcases.demo.conf import test_Configuration_information

site = test_Configuration_information.site
all_case="baidu_select_test"
title="Demo Test"
tester="liuss"
control.control(site,all_case,title,tester)

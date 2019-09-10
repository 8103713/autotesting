__author__ = 'liuss'

#coding:utf-8

from controller import control
from testcases.HLJ_CRM60.conf import test_Configuration_information

site = test_Configuration_information.site
all_case="aut_4660_YXZX"
title="Demo Test"
tester="liuss"
control.control(site,all_case,title,tester)

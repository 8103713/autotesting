__author__ = 'liuss'
# -*- coding: utf-8 -*-

import unittest
import json
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from testcases.demo.operation import public_operation, baidu_operation
from public import test_UIbase
from testcases.demo.conf import test_Configuration_information


class baidu_select_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.Log=test_Configuration_information.LogConfig.Log
        self.Log.info("=====Start baidu_select_test=====")

        #get case config
        self.site = test_Configuration_information.site
        self.platform = test_Configuration_information.platform
        self.baseurl = test_Configuration_information.UrlConfig.baseurl

        #Get PageOperation Function
        self.PageOperation = test_UIbase.PageOperation()


        #start driver
        self.driver = self.PageOperation.ChoseDriver(self.platform)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(self.baseurl)

    def test_Select01(self):
        self.Log.info("test_Select01 start-->")

        #使用SelectText数据文件执行测试
        datapath = "data\\SelectText.data"
        testdataseq = 0 #0-随机

        TestData = test_UIbase.GetTestData(self.site,datapath,testdataseq)
        Data = TestData.GetData().split(',')
        select=Data[0]

        #测试数据json格式转换
        self.test_data = json.dumps({"select":select})
        self.Log.debug("test data:"+format(self.test_data))

        #调用测试用例
        self.PageOperation.excutecase(baidu_operation.selectTest,
                                      test_Configuration_information.ScreenShot.ScreenShotPath,
                                      self.driver,
                                      self.test_data)
        self.Log.info("test_Select01 finish##")

    def test_Select02(self):
        self.Log.info("test_Select02 start-->")

        #使用SelectText数据文件执行测试
        datapath = "data\\SelectText.data"
        testdataseq = 1 #1-取第一行数据

        TestData = test_UIbase.GetTestData(self.site,datapath,testdataseq)
        Data = TestData.GetData().split(',')
        select=Data[0]

        #测试数据json格式转换
        self.test_data = json.dumps({"select":select})

        """
        #调用公共方法拼装测试数据
        datapath = "SelectText"
        testdataseq = 2
        datas=[(datapath,testdataseq)]
        test_data=public_operation.getTestData(self.site,datas)
        """


        self.Log.debug("test data:"+format(self.test_data))

        #调用测试用例
        self.PageOperation.excutecase(baidu_operation.selectTest,
                                      test_Configuration_information.ScreenShot.ScreenShotPath,
                                      self.driver,
                                      self.test_data)
        self.Log.info("test_Select02 finish##")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.assertEqual([], self.verificationErrors)
        """
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            self.driver.save_screenshot("Screenshots/%s.png" % test_method_name)
        """

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
        self.Log.info("=====Finish demoTest=====")


if __name__ == "__main__":
    unittest.main()

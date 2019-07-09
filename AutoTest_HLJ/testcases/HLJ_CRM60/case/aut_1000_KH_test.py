# -*- coding: utf-8 -*-

import unittest

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from public import test_UIbase
from testcases.HLJ_CRM60.conf import test_Configuration_information
from testcases.HLJ_CRM60.operation import public_operation,aut_1000_KH

class baidu_select_test(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.Log=test_Configuration_information.LogConfig.Log
        self.Log.info("=====Start aut_1000_KH_test=====")

        #get case config
        self.site = test_Configuration_information.site
        self.platform = test_Configuration_information.platform
        self.base_url = test_Configuration_information.UrlConfig.base_url
        self.city_code = test_Configuration_information.CityConfig.city_code
        self.op_code_check_tag = test_Configuration_information.checkTag.QuickSearch

        #Get PageOperation Function
        self.PageOperation = test_UIbase.PageOperation()

        #start driver
        self.driver = self.PageOperation.ChoseDriver(self.platform)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.get(self.base_url)

        #login
        user_name=test_Configuration_information.userName(self.city_code)
        user_password=test_Configuration_information.userPwd(self.city_code)
        public_operation.loginCRM(self.driver,user_name,user_password)
        #unittest.skipUnless(public_operation.loginCRM(self.driver,user_name,user_password),"login fail!")

    def setUp(self):
        #进入1000功能页面
        op_code="1000"
        public_operation.quickSearch(self.driver,op_code,self.op_code_check_tag)

    #@unittest.skipUnless(setUp,"quick search fail")
    def test_01(self):
        self.Log.info("test_01 start-->")


        #调用公共方法拼装测试数据
        datapath = "cust_info"
        testdataseq = 2
        datas=[(datapath,testdataseq)]
        test_data=public_operation.getTestData(self.site,datas)
        self.Log.debug("test data:"+format(test_data))

        #调用测试用例
        self.PageOperation.excutecase(aut_1000_KH.newCustomer,
                                      test_Configuration_information.ScreenShot.ScreenShotPath,
                                      self.driver,
                                      test_data)
        self.Log.info("test_01 finish##")

        print("ok")

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
        public_operation.closeOPFrame(self.driver)
        self.assertEqual([], self.verificationErrors)
        """
        if sys.exc_info()[0]:
            test_method_name = self._testMethodName
            self.driver.save_screenshot("Screenshots/%s.png" % test_method_name)
        """

    @classmethod
    def tearDownClass(self):
        #self.driver.quit()
        self.Log.info("=====Finish aut_1000_KH_test=====")


if __name__ == "__main__":
    unittest.main()

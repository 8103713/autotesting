__author__ = 'thinkpad'

import json
from public import test_UIbase
from testcases.demo.conf import test_Configuration_information

PageOperation = test_UIbase.PageOperation()
Log=test_Configuration_information.LogConfig.Log

def selectTest(driver,data):
    #获取测试数据
    testData = json.loads(data)
    selectText=testData["select"]

    #页面赋值及元素操作
    PageOperation.InsertData(driver,selectText,'input','id','kw')
    PageOperation.ClickButton(driver,'input','id','su')

    #获取页面元素内容
    tagText = PageOperation.GetText(driver,'span','class','nums_text')
    Log.debug("tagText"+format(tagText))

    #判断页面元素是否正确
    tarText="百度为您找到相关结果"
    PageOperation.caseYN(driver,tarText in tagText,'baiduSelect fail')


if __name__ == "__main__":
    driver=PageOperation.ChoseDriver("firefox")
    driver.get("http://www.baidu.com")
    data=json.dumps({"select":"test"})
    selectTest(driver,data)



__author__ = 'liuss'

import json,time

from public import test_UIbase

from selenium import webdriver
from testcases.HLJ_CRM60.conf import test_Configuration_information

PageOperation = test_UIbase.PageOperation()
"""
    #拼装测试数据
    #datas=[(dataName,dataSeq)]
    #可实现从多个data文件获取数据并拼装成一条测试数据返回
"""
def getTestData(site,datas):
    paramName=[]
    paramValu=[]
    for i in datas:
        dataName=i[0]
        dataSeq=i[1]
        if dataName=="phone_no":
            paramName.append("no_type")
            paramName.append("cust_phone_no")
        elif dataName=="cust_info":
            paramName.append("id_card_type")
            paramName.append("id_card_no")
            paramName.append("cust_name")
            paramName.append("id_card_addr")
            paramName.append("contact_phone_no")
            paramName.append("cust_nation")
            paramName.append("issuing_authority")

        datapath = "data\\"+dataName+".data"
        TestData = test_UIbase.GetTestData(site,datapath,dataSeq)
        Data = TestData.GetData().split(',')
        for j in Data:
            paramValu.append(j)
    testData={}

    for i in range(0,len(paramName),1):
        testData[paramName[i]]=paramValu[i]

    test_data = json.dumps(testData)

    return test_data

"""
    #登录CRM
    #user_name/user_password:配置文件配置，根据地市代码获取
    #return:True/False
"""
def loginCRM(driver,user_name,user_password):
    PageOperation.InsertData(driver,user_name,'input','id','userName')
    PageOperation.InsertData(driver,user_password,'input','id','password')
    PageOperation.ClickButton(driver,'button','id','login-button')
    PageOperation.SwitchWindow(driver)
    tagText = PageOperation.GetText(driver,'div','id','myinfo')
    return user_name in tagText

"""
    #进入客户首页
    #no_type:号码类型，读取测试数据
    #cust_no:服务号码，读取测试数据
    #return:True/False
"""
def loginCust(driver,no_type,cust_no):
    PageOperation.WriteHideText(driver,no_type,"input","id","loginType")
    PageOperation.InsertData(driver,cust_no,'input','id','J_opSchServIpt')
    PageOperation.ClickButton(driver,'button','id','J_opSchServBtn')
    tagText = PageOperation.GetText(driver,'ul','id',"J2_opIframe0")
    tarText="客户首页"
    return tarText in tagText

"""
    #输入op_code进入功能页面
    #div_id:校验点定位标识,配置文件checkTag中配置
    #return:True/False
"""
def quickSearch(driver,op_code,div_id):
    time.sleep(5)
    PageOperation.InsertData(driver,op_code,'input','id','quickSearch')
    PageOperation.ClickButton(driver,'button','id','quickSearchBtn')
    PageOperation.Switch2Iframe(driver,"iframe","opcode",op_code)
    tagText = PageOperation.GetText(driver,'div','id',div_id)
    return op_code in tagText

"""
    #关闭功能页面
"""
def closeOPFrame(driver):
    PageOperation.SwitchOutIframe(driver)
    PageOperation.ClickButton(driver,'img','class','close-btn')

if __name__ == "__main__":
    driver=webdriver.Chrome()
    driver.get("http://10.149.85.39:46000/eppage/login.html")

    city_code = test_Configuration_information.CityConfig.city_code
    user_name=test_Configuration_information.userName(city_code)
    user_password=test_Configuration_information.userPwd(city_code)
    print("login")
    print(loginCRM(driver,user_name,user_password))
    print("phone")
    #print(loginCust(driver,"1","13796673965"))
    #print(loginCust(driver,"4","4510988975"))
    print("opcode")
    print(quickSearch(driver,"3839","2000072261"))
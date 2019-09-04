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
        if dataName=="jiaofei":
            paramName.append("phone_no")
            paramName.append("charge")
        elif dataName=="cust_info":
            paramName.append("id_card_type")
            paramName.append("id_card_no")
            paramName.append("cust_name")
            paramName.append("id_card_addr")
            paramName.append("contact_phone_no")
            paramName.append("bak1")
            paramName.append("bak2")

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
def quickSearch(driver,op_code,div_id,wait=True):
    if wait:
        time.sleep(10)
    PageOperation.InsertData(driver,op_code,'input','id','quickSearch')
    PageOperation.ClickButton(driver,'button','id','quickSearchBtn')
    PageOperation.Switch2Iframe(driver,"iframe","opcode","8000")
    tagText = PageOperation.GetText(driver,'div','id',div_id)
    return op_code in tagText

"""
    #关闭功能页面
"""
def closeOPFrame(driver,op_code):
    PageOperation.SwitchOutIframe(driver)
    PageOperation.ClickButton(driver,'img','class','close-btn',"opcode",op_code)

"""
    #获取证件类型列表顺序
"""
def getIdTypeIndex(id_type):
    id_types=test_Configuration_information.IndexConfig.id_types
    return id_types.index(id_type)

"""
    #验证订单执行状态
    #div_id:校验点定位标识,配置文件checkTag中配置
    return:(True/False,msg)
"""
def checkOrderStatus(driver,order_id,div_id):
    op_code="5730"
    msg=''
    result=True
    if quickSearch(driver,op_code,div_id,False):
        PageOperation.InsertData(driver,order_id,'input','name','searchInput')
        n=0
        while result:
            PageOperation.ClickButton(driver,'button','name','searchButton')
            """div[identify=order_id]>div>div>div>div>table>tbody>tr[copy_sign='0']>td[name='orderState']"""
            css_path="div>div>div>div>table>tbody>tr[copy_sign='0']>td[name='orderState']"
            tagText=PageOperation.GetText(driver,"div","identify",order_id,path=css_path)
            tarText="已撤单"
            tempText="处理中"
            if tarText in tagText:
                msg="订单[%s]处理状态:%s" %(order_id,tagText)
                result=False
            elif tempText in tagText:
                time.sleep(1)
                n += 1
                msg="订单[%s]处理状态:%s" %(order_id,tagText)
                if n == 60:
                    result=False
            else:
                msg="订单[%s]处理状态:%s" %(order_id,tagText)
                break
        closeOPFrame(driver,op_code)
    else:
        msg="无法查询订单[%s]处理状态" %order_id
        result=False
    return (result,msg)

if __name__ == "__main__":

    driver=webdriver.Firefox()
    driver.get("http://10.149.85.39:46000/eppage/login.html")
    loginCRM(driver,"aheb05","111111")
    time.sleep(5)

    div_id="2000072261"
    #order_id="O19041900000229"
    #print(checkOrderStatus(driver,order_id,div_id))
    #order_id="O19022100000193"
    #print(checkOrderStatus(driver,order_id,div_id))
    order_id="O19062700000695"
    print(checkOrderStatus(driver,order_id,div_id))
import json,time
from selenium.webdriver.common.action_chains import ActionChains
from public import test_UIbase
from testcases.demo.conf import test_Configuration_information
from selenium.webdriver.common.keys import Keys
from testcases.HLJ_CRM60.operation import public_operation

PageOperation = test_UIbase.PageOperation()
Log=test_Configuration_information.LogConfig.Log

def newCustomer(driver,data):
    #获取测试数据
    testData = json.loads(data)
    cust_name = testData["cust_name"]
    id_card_no = testData["id_card_no"]
    id_card_addr = testData["id_card_addr"]
    contact_phone_no = testData["contact_phone_no"]
    #cust_nation = testData["bak1"]
    #issuing_authority = testData["bak2"]
    cust_nation = testData["cust_nation"]
    issuing_authority = testData["issuing_authority"]

    #输入数据

    PageOperation.InsertData(driver, cust_name, 'input', 'name', 'CUST_NAME')
    PageOperation.InsertData(driver, id_card_no, 'input', 'name', 'ID_ICCID')
    PageOperation.InsertData(driver, id_card_addr, 'input', 'name', 'ID_ADDRESS')
    PageOperation.InsertData(driver, contact_phone_no, 'input', 'name', 'CONTACT_PHONE')
    PageOperation.InsertData(driver, cust_nation, 'input', 'name', 'NATION')
    PageOperation.InsertData(driver, issuing_authority, 'input', 'name', 'ISSUING_AUTHORITY')
    PageOperation.ClickButton(driver, 'button', 'name', 'butt_next')
    PageOperation.ClickButton(driver, 'button', 'name', 'BTN_MORE')


    PageOperation.SwitchOutIframe(driver)
    aria_describedby=PageOperation.GetAttrValue(driver,'aria-describedby','div','role','alertdialog')
    iframe_name=aria_describedby.split(':')[1]
    PageOperation.Switch2Iframe(driver,'iframe','name',iframe_name)
    time.sleep(3)
    ele = driver.find_element_by_id('2000007910')
    action = ActionChains(driver)
    action.move_to_element(ele).perform()
    action.click(ele).perform()
    time.sleep(3)
    PageOperation.InsertData(driver, "JZTK38Y", "input", "id", "2000007910")
    time.sleep(4)
    driver.find_element_by_id("2000007910").send_keys(Keys.ENTER)
    #PageOperation.ClickButton(driver,'button','name','BTN_CONFIRM')
    PageOperation.SwitchOutIframe(driver)
    PageOperation.Switch2Iframe(driver, 'iframe', 'name', 'iframe"1000"')
    PageOperation.ClickButton(driver,'button','id','300172557')

    PageOperation.SelectList(driver,'1','select','id','300202302')
    PageOperation.ClickButton(driver,'button','id','10416')

    #切iframe
    PageOperation.SwitchOutIframe(driver)
    aria_describedby = PageOperation.GetAttrValue(driver, 'aria-describedby', 'div', 'role', 'alertdialog')
    iframe_name = aria_describedby.split(':')[1]
    PageOperation.Switch2Iframe(driver, 'iframe', 'name', iframe_name)
    #全部号码
    driver.find_element_by_xpath('//*[@id="41587"]/div/div/table/tbody/tr[1]/td[2]/label[4]').click()
    #选号
    driver.find_element_by_xpath('//*[@id="12118"]/span[1]/label').click()
    time.sleep(2)
    PageOperation.ClickButton(driver, 'button', 'id', '10460')

    PageOperation.SwitchOutIframe(driver)
    PageOperation.Switch2Iframe(driver, 'iframe', 'name', 'iframe"1000"')
    #选卡
    PageOperation.ClickButton(driver, 'button', 'id', '10419')
    #切到选卡弹窗
    PageOperation.SwitchOutIframe(driver)
    aria_describedby = PageOperation.GetAttrValue(driver, 'aria-describedby', 'div', 'role', 'alertdialog')
    iframe_name = aria_describedby.split(':')[1]
    PageOperation.Switch2Iframe(driver, 'iframe', 'name', iframe_name)
    #定位的方式选卡
    driver.find_element_by_xpath('//*[@id="41588"]/div/div/table/tbody/tr[1]/td[2]/label[3]').click()
    driver.find_element_by_xpath('//*[@id="12092"]/span[1]/label').click()
    time.sleep(2)
    #选完提交
    PageOperation.ClickButton(driver, 'button', 'id', '10732')
    #切回1000办理页面
    PageOperation.SwitchOutIframe(driver)
    PageOperation.Switch2Iframe(driver, 'iframe', 'name', 'iframe"1000"')
    time.sleep(2)
    PageOperation.InsertData(driver, "147852", "input", "id", "2000042064")
    PageOperation.InsertData(driver, "147852", "input", "id", "2000042068")
    PageOperation.ClickButton(driver, 'button', 'name', 'directsubCommon')







    #driver.switch_to.frame(driver.find_element_by_name('1561686170936'))
    # 获取当前窗口句柄
    ##driver.switch_to.window(h[-1])
    #driver.switch_to_frame("1561686170937")
    #PageOperation.AlertAccept(driver)
    #PageOperation.SwitchWindow(driver)
    #PageOperation.Switch2Iframe(driver, 'iframe', 'name', '1561686170937')
    #PageOperation.SwitchOutIframe(driver)





    #获取页面元素内容
    tagText = PageOperation.GetText(driver,'b','class','title fl')
    Log.debug("tagText"+format(tagText))

    #判断页面元素是否正确
    tarText="产品选择"
    PageOperation.caseYN(driver,tarText in tagText,'Product selection fail')




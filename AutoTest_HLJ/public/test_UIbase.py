__author__ = 'tabsang'
# -*- coding: utf-8 -*-
import os

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


'''Basic function'''



#Anomaly class

def ChosePath():
    '''return the path of project'''
    env_dist = os.environ
    lists = env_dist.get("path").split(";")

    path = ''
    for i in lists:
        if 'python' in i or 'Python' in i:
            if 'script' not in i and 'Script' not in i and 'site-packages' not in i:
                path = i
    currentpathlist = os.getcwd().split(os.sep)
    if "testcases" in currentpathlist:
        tarindex = currentpathlist.index("testcases")
    if "public" in currentpathlist:
        tarindex = currentpathlist.index("public")
    if "controller" in currentpathlist:
        tarindex = currentpathlist.index("controller")
    tarfile = currentpathlist[tarindex - 1] + ".pth"
    tarpath = path + os.sep + "Lib" + os.sep + "site-packages" + os.sep + tarfile
    with open(tarpath) as f:
        lines = f.readlines()
    return lines[0].strip() + os.sep



def logconfig(logpath,level):
    import logging
    handler = logging.FileHandler(logpath, "a",encoding = "UTF-8")
    formatter = logging.Formatter('%(asctime)s %(filename)s[line:%(lineno)d] %(funcName)s %(levelname)s %(message)s')
    handler.setFormatter(formatter)
    root_logger = logging.getLogger()
    root_logger.addHandler(handler)
    if level == "debug":
        root_logger.setLevel(logging.DEBUG)
    if level == "info":
        root_logger.setLevel(logging.INFO)
    if level == "warning":
        root_logger.setLevel(logging.WARNING)
    return root_logger



class ElementNotExist(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

def CurrentPath():
    '''Get the current path'''
    return os.getcwd() + os.sep

def CurrentTime(format):
    '''
        Get the current time [%Y%m%d-%H%M%S]
        format:format of return
    '''
    now = datetime.datetime.now()
    recice_time = now.strftime("%s" % format)
    return recice_time

class GetTestData:
    def __init__(self,site,tarfile,seq):
        self.seq = seq
        self.tar = self._LocalCaseDirection(site,tarfile)

    def _LocalCaseDirection(self,site,tarfile):
        '''Return the cases config path'''
        path = ChosePath()
        return path + "testcases" + os.sep + site + os.sep + tarfile

    def GetData(self):
        '''Get test data'''
        import random
        import platform
        version = platform.python_version().split(".")[0]
        lines = []
        if version == "3":
            with open(self.tar,"r",encoding= 'utf-8') as f:
                lines = f.readlines()
        if version == "2":
            with open(self.tar,"r") as f:
                lines = f.readlines()
        if self.seq != 0:
            return lines[int(self.seq)].strip()
        else:
            return lines[random.choice(range(1,len(lines)))].strip()

class TestDataConstruction:
    #15 bit random number
    def CreatRandom(self,num):
        import random
        source = "01234567890123456789012345678901234567890123456789"
        string = ''
        Trandom = string.join(random.sample(source, num))
        return Trandom

    #CurrentTime[%Y%m%d-%H%M%S]
    def CurrentTime(self,format):
        now = datetime.datetime.now()
        recice_time = now.strftime("%s" % format)
        return recice_time

    def Tendays(self,format):
        tar_day = ''
        tar_month = ''
        thirty_one = [1,3,5,7,8,10,12]
        thirty = [4,6,9,11]
        currenttime = self.CurrentTime(format)
        currentyear = currenttime.split("-")[0]
        currentmonth = int(currenttime.split("-")[1])
        currentday = int(currenttime.split("-")[-1])
        if currentmonth in thirty_one:
            if currentday + 10 <= 31:
                tar_day = str(currentday + 10)
                tar_month = str(currentmonth)
            if currentday + 10 > 31:
                tmp_tar_month = currentmonth + 1
                if tmp_tar_month > 12:
                    tar_month = str(currentmonth)
                    tar_day = str(31)
                else:
                    tar_day = str(currentday + 10 - 31)
                    tar_month = str(currentmonth + 1)
        if currentmonth in thirty:
            if currentday + 10 <= 30:
                tar_day = str(currentday + 10)
                tar_month = str(currentmonth)
            if currentday + 10 > 30:
                tar_day = str(currentday + 10 - 30)
                tar_month = str(currentmonth + 1)
        if currentmonth == 2:
            if currentday + 10 <= 28:
                tar_day = str(currentday + 10)
                tar_month = str(currentmonth)
            if currentday + 10 > 28:
                tar_day = str(currentday + 10 - 28)
                tar_month = str(currentmonth + 1)
        return currentyear + "-" + tar_month + "-" + tar_day

class LocatingElement:
    def FindById(self,driver, id):
        '''
            Encapsulation of find_element_by_id
            driver:Browser handle
            id:string, element ID
        '''
        element = driver.find_element_by_id(id)
        return element

    def FindsByCss(self,driver, css):
        '''
            Encapsulation of find_elements_by_css_selector
            driver:Browser handle
            css:string, element css
        '''

        returnelement = []
        elements = driver.find_elements_by_css_selector(css)
        for i in elements:
            if i and i.is_enabled() and EC.visibility_of(i):
               returnelement.append(i)

        return returnelement
        #elements = driver.find_elements_by_css_selector(css)
        #return elements

    def FindByCss(self,driver, css):
        '''
            Encapsulation of find_element_by_css_selector
            driver:Browser handle
            css:string, element css
        '''
        element = driver.find_element_by_css_selector(css)
        return element

    def FindByClassName(self,driver, classname):
        '''
            Encapsulation of find_element_by_class_name
            driver:Browser handle
            classname:string, element classname
        '''
        element = driver.find_element_by_class_name(classname)
        return element

    def FindByName(self,driver, name):
        '''
            Encapsulation of find_element_by_name
            driver:Browser handle
            name:string, element name
        '''
        element = driver.find_element_by_name(name)
        return element

    def FindsByName(self,driver, name):
        '''
            Encapsulation of find_elements_by_name
            driver:Browser handle
            name:string, element name
        '''
        elements = driver.find_elements_by_name(name)
        return elements

    def FindByLinktext(self,driver, content):
        '''
            Encapsulation of find_element_by_link_text
            driver:Browser handle
            content:string, element link text
        '''
        element = driver.find_element_by_link_text(content)
        return element

    def FindByXpath(self,driver, content):
        '''
            Encapsulation of find_element_by_xpath
            driver:Browser handle
            content:string, element xpath
        '''
        element = driver.find_element_by_xpath(content)
        return element

class ConFigure:
    '''
        Read the configuration file
        tarfile:target conf
    '''
    def __init__(self,site,tarfile):
        import platform
        version = platform.python_version().split(".")[0]
        if version == "2":
            import ConfigParser
            self.tarfile = self._LocalCaseDirection(site,tarfile)
            self.cf = ConfigParser.RawConfigParser()
        if version == "3":
            import configparser
            self.tarfile = self._LocalCaseDirection(site,tarfile)
            self.cf = configparser.RawConfigParser()
        self.cf.read(self.tarfile)

    def _LocalCaseDirection(self,site,tarfile):
        '''Return the cases config path'''
        path = ChosePath()
        return path + "testcases" + os.sep + site + os.sep + tarfile

    def readconfig(self,session,option):
        '''
            readconfig
            session: name of session
            operation: key of operation
        '''
        return self.cf.get(session, option)

    def alterfig(self,session,option,value):
        '''
            alert config
            session: name of session
            operation: key of operation
            value: target value
        '''
        self.cf.set(session,option,value)
        self.cf.write(open(self.tarfile, "wb"))

    def addoption(self,session,option,value):
        '''
            add operation
            session: name of session
            operation: name of add operation
            value: target value
        '''
        self.cf.set(session,option,value)
        self.cf.write(open(self.tarfile, "wb"))

    def addsession(self,addsession,option,value):
        '''
            add session
            addsession: name of addsession
            operation: name of add operation
            value: target value
        '''
        self.cf.add_section(addsession)
        self.cf.set(addsession, option, value)


LocatingElement = LocatingElement()

class PageOperation:

    def _IframeLocate(self,driver, iframe):
        '''
            switch iframe
            driver:Browser handle
            iframe:tar iframe
        '''
        driver.switch_to.frame(iframe)

    def _GoPages(self,driver,value):
        '''
            Page scrolls to the target location 0 for top or 1000 for bottom
            driver:Browser handle
            value:Target element
        '''
        js = "var q=document.documentElement.scrollTop=%s" % value
        driver.execute_script(js)

    def GetWeb(self,driver,url):
        '''
            Input address
            driver:Browser handle
            url:String, URL to be accessed
        '''
        driver.get(url)
        tartext = self.GetText(driver,'!','id','usersso')
        self.caseYN(driver,'用户登录' in tartext,"get web fail")

    def IsElementExist(self,driver,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Determine whether the element exists
            driver:Browser handle
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:select a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        tarcount = 0

        tar = []
        cssselector = ''
        if not path and not findtype2:
            if labeltag.startswith('!'):
                cssselector = "[%s='%s']" % (findtype1,value1)
            else:
                cssselector = "%s[%s='%s']" % (labeltag,findtype1,value1)
        if not path and findtype2:
            if labeltag.startswith('!'):
                cssselector = "[%s='%s'][%s='%s']" % (findtype1,value1,findtype2,value2)
            else:
                cssselector = "%s[%s='%s'][%s='%s']" % (labeltag,findtype1,value1,findtype2,value2)
        if path and not findtype2:
            if labeltag.startswith('!'):
                cssselector = "[%s='%s']>%s" % (findtype1,value1,path)
            else:
                cssselector = "%s[%s='%s']>%s" % (labeltag,findtype1,value1,path)
        if path and findtype2:
            if labeltag.startswith('!'):
                cssselector = "[%s='%s'][%s='%s']>%s" % (findtype1,value1,findtype2,value2,path)
            else:
                cssselector = "%s[%s='%s'][%s='%s']>%s" % (labeltag,findtype1,value1,findtype2,value2,path)
        if findtype2 and value2:
            if findtype2.startswith('!') or value2.startswith('!'):
                if labeltag.startswith('!'):
                    cssselector = "[%s='%s']" % (findtype1,value1)
                else:
                    cssselector = "%s[%s='%s']" % (labeltag,findtype1,value1)

        #"div[class='col-sm-7 col-md-7'][id='fuwuhaoma_app']>div[name='logType1']>div[id='activeCustDetail']>input"
        #        css1 = "div[id='u1']>a"
        #css2 = "div[class='head_wrapper']>div:nth-child(3)>a"
        while 1:
            tar = LocatingElement.FindsByCss(driver,cssselector)
            if len(tar) != 0:
                if findtype2 and value2:
                    if value2.startswith('!') and not findtype2.startswith("!"):
                        novalue2 = []
                        for i in tar:
                            exceptvalue = i.get_attribute(findtype2)
                            if len(exceptvalue) != 0 and exceptvalue != value2[1:]:
                                novalue2.append(i)
                        tar = novalue2
                    if findtype2.startswith("!"):
                        notype = []
                        for j in tar:
                            excepttype = j.get_attribute(findtype2[1:])
                            if len(excepttype) == 0:
                                notype.append(j)
                        tar = notype
                break
            tarcount += 1
            if tarcount > count:
                break
            time.sleep(0.5)

        if len(tar) == 1:
            return True, tar
        elif len(tar) > 1:
            if chose != 0:
                return True, tar[sequence]
            else:
                return True, tar
        else:
            content = "[%s]%s==>%s,%s==>%s" % (count,findtype1,value1,findtype2,value2)
            if failreturn == 0:
                content = "[%s]%s==>%s,%s==>%s" % (count,findtype1,value1,findtype2,value2)
                raise ElementNotExist(content + 'element not exist')
            else:
                return False,content

    def GoToPages(self,driver,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Roll to the desired position
            driver:Browser handle
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        target = ''
        tar = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if tar[0]:
            target = tar[1][0]
        driver.execute_script("arguments[0].scrollIntoView();", target)

    def InsertData(self,driver,content,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Inserting data into a text box
            driver:Browser handle
            content:Inserted content
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        element = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if element[0]:
            time.sleep(0.5)
            driver.execute_script("arguments[0].scrollIntoView();", element[1][0])
            element[1][0].clear()
            element[1][0].send_keys(content)

    def Submit(self,driver,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Carry out the return operation
            driver:Browser handle
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        element = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if element[0]:
            time.sleep(0.5)
            driver.execute_script("arguments[0].scrollIntoView();", element[1][0])
            element[1][0].send_keys(Keys.ENTER)

    def InsertsData(self,driver,intype,invalue,content,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Find the execution target from multiple input boxes and enter the content
            driver:Browser handle
            intype:Locate the attribute of the target input box
            invalue:Locate the value of the target input box attribute to the value used
            content:Input content
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        elements = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if elements[0]:
            for element in elements:
                if element.get_attribute(intype) == invalue:
                    time.sleep(0.5)
                    element.clear()
                    driver.execute_script("arguments[0].scrollIntoView();", element)
                    element.send_keys(content)

    def ClickButton(self,driver,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            ClickButton
            driver:Browser handle
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        import random
        element = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if element[0]:
            driver.execute_script("arguments[0].scrollIntoView();", element[1][0])
            time.sleep(0.5)
            count = 0
            while 1:
                try:
                    if chose != 0:
                        element[1][sequence].click()
                    else:
                        a = random.choice(range(0,len(element[1])))
                        element[1][a].click()
                    break
                except Exception as e:
                    count += 1
                    if count > 5:
                        raise Exception(str(e))
                    pass
                time.sleep(0.5)


    def GetAttrValue(self,driver,attribute,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            ClickButton
            driver:Browser handle
            attribute:attributes
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        Value = ''
        element = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if element[0]:
            Value = element[1][0].get_attribute(attribute)
        if attribute == 'innerHTML':
            return Value
        else:
            return Value.strip()

    def JudgeAttrValue(self,driver,tartype,tarvalue,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Determine whether the attribute value is the target value
            driver:Browser handle
            tartype:Attribute of target value
            tarvalue:target value
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        count1 = 0
        while 1:
            attr = self.GetAttrValue(driver,tartype,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
            tar = attr.split()[1]
            if tar == tarvalue:
                break
            count1 += 1
            if count1 > 10:
                raise ElementNotExist('pages load fail')
            time.sleep(0.5)
        return True

    def JudgeTextValue(self,driver,targetvalue,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Determine whether the text value is the target value and return the (True,text)
            driver:Browser handle
            targetvalue:target value
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        count1 = 0
        tarphone = ''
        while 1:
            time.sleep(2)
            tarphone = self.GetText(driver,labeltag,findtype1,value1,findtype2,value2,path,chose,sequence,count,failreturn)
            if len(tarphone) != 0 and tarphone == targetvalue:
                break
            count += 1
            if count1 > 10:
                raise ElementNotExist('can not find target value')
        return tarphone.strip()



    def GetText(self,driver,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Getting the text value of an element
            driver:Browser handle
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        Text = ''
        element = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if element[0]:
            if len(element[1]) == 1:
                Text = element[1][0].text
            else:
                for i in element[1]:
                    Text += i.text + '\n'
        return Text.strip()


    def Switch2Iframe(self,driver,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            switch iframe
            driver:Browser handle
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:select a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        element = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if element[0]:
            self._IframeLocate(driver,element[1][0])


    def SwitchOutIframe(self,driver):
        '''
        quit iframe
        driver:Browser handle
        '''
        driver.switch_to_default_content()



    def SelectList(self,driver,num,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        '''
            Select options
            driver:Browser handle
            num：Select the seq of element
            labeltag:name of html tag
            findtype1:The attribute of the label
            value1:Attribute value
            findtype2:The second attributes of the tag, the default is 0
            value2:The value of the second attributes, the default is 0
            path:Relative path of locating elements
            chose:elect a number of elements，chose=1 to Switch on the selected switch
            sequence:Used with chose, indicating which element to select, by default of 0
            count:the count of Finding elements, the default 15
            failreturn:After the location element fails, 0 for reporting exceptions, 1 for
                        returnningto False, and the default is 0.
        '''
        element = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if element[0]:
            time.sleep(1.5)
            Select(element[1][0]).select_by_index(num)

    def caseYN(self,driver, condition, content):
        '''
            Determine whether the use case is successful
            driver:Browser handle
            condition:A==B,Contrast between expected data and actual data
            content:The return value after the use case fails
        '''
        if driver is None or driver == []:
            assert condition, content
        else:
            assert condition, content

    def SwitchWindow(self,driver,flog=0,pages=1):
        '''
            Switch the windows window
            driver:Browser handle
            flog：
            pages：
        '''
        time.sleep(3)
        try:
            now_handle = driver.current_window_handle
            all_handles = driver.window_handles

            for handle in all_handles:
                if handle != now_handle:
                    driver.switch_to_window(handle)
        except:
            all_handles = driver.window_handles
            if len(all_handles) == 1:
                driver.switch_to_window(all_handles[0])

    def excutecase(self,func,screenpath,driver,tarjson):
        '''excuting the call case'''
        try:
            func(driver,tarjson)
        except Exception as e:

            self.WebScreenShot(driver,screenpath,"test_%s.png"% func.__name__)
            self.caseYN(driver,False,str(e))
            raise Exception(str(e))


    def AlertAccept(self,driver):
        '''js alert Accept'''
        alert = driver.switch_to_alert()
        time.sleep(1)
        alert.accept()


    def AlertDismiss(self,driver):
        '''js alert cancel'''
        alert = driver.switch_to_alert()
        time.sleep(1)
        alert.dismiss()


    def AlertText(self,driver):
        '''JS alert value'''
        alert = driver.switch_to_alert()
        time.sleep(1)
        alerttext = alert.text
        return alerttext

    #获取输入框input中的输入值
    def GetvalueByJs(self,driver,type,tarvalue):
        '''
            Get the value of the element by JS
            driver:Browser handle
            id:string, element ID
        '''
        js = ''
        if type == 'id':
            js = "return document.getElementById('%s').value" % tarvalue
        if type == 'class':
            js = "return document.getElementByClassName('%s').value" % tarvalue
        value = driver.execute_script(js)
        return value





    def ChoseDriver(self,platform):
        '''
            Start the browser
            platform:the type of browser
        '''
        if platform.lower() == "chrome":
            #operation= webdriver.ChromeOptions()
            #operation.add_argument('--user-data-dir=C:\\Users\FF\AppData\Local\Google\Chrome\\User Data') #设置成用户自己的数据目录
            #driver = webdriver.Chrome(chrome_options=operation)
            #driver = webdriver.Chrome()
            option = webdriver.ChromeOptions()
            option.add_argument('--disable-popup-blocking')
            option.add_argument('disable-infobars')
            driver = webdriver.Chrome(chrome_options=option)
        elif platform.lower() == "ie":
            iedriver = "C:\Program Files (x86)\Internet Explorer\IEDriverServer.exe"
            os.environ["webdriver.ie.driver"] = iedriver
            driver = webdriver.Ie(iedriver)
            #driver = webdriver.Ie()
        else:
            profile = webdriver.FirefoxProfile()
            profile.set_preference("browser.startup.homepage", "about:blank")
            profile.set_preference("startup.homepage_welcome_url", "about:blank")
            profile.set_preference("startup.homepage_welcome_url.additional", "about:blank")
            driver = webdriver.Firefox(profile)
        driver.maximize_window()
        #driver.set_window_size(400,900)
        driver.implicitly_wait(5)
        return driver

    def WebScreenShot(self,driver,path,name):
        '''
            Web screenshot
            driver:Browser handle
            name:The name of the screenshot
        '''
        tarshot = path + name
        driver.get_screenshot_as_file(tarshot)

    def WriteHideText(self,driver,msg,labeltag,findtype1,value1,findtype2=None,value2=None,path=None,chose=0,sequence=0,count=15,failreturn=0):
        element = self.IsElementExist(driver,labeltag,findtype1,value1,findtype2=findtype2,value2=value2,path=path,chose=chose,sequence=sequence,count=count,failreturn=failreturn)
        if element[0]:
            time.sleep(0.5)
            driver.execute_script("arguments[0].scrollIntoView();", element[1][0])
            driver.execute_script("arguments[0].setAttribute('value','%s');" %(msg), element[1][0])

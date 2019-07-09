__author__ = 'liuss'

from public import test_UIbase
import json

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
        if dataName=="SelectText":
            paramName.append("select")
        elif dataName=="xxx":
            paramName.append("A1")
            paramName.append("A2")

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

if __name__ == "__main__":
    site="demo"
    datapath = "SelectText"
    testdataseq = 2
    datas=[(datapath,testdataseq)]
    test_data=getTestData(site,datas)
    print(format(test_data))
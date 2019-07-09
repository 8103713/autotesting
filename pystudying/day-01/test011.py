#coding:utf-8
"""if判断语句学习"""
age = int(input("请输入你的年龄： "))
if(age >= 0 and age <= 120):
    #条件1基础上的条件2
    if(age >= 18):
        print("滚进网吧high去吧！")
    else:
        print("自己多大没点数吗？")
else:
    print("别瞎输入好吗？？？")

print("----------")
#elif是多个平级条件的判断
if(age == 17):
    print("18岁那年的雨季")
elif(age == 30):
    print("30而立")
else:
    print("心咋这大呢，还去网吧")
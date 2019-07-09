#coding:utf-8
"""
python学习第一天，乱七八糟
"""
name = "老K"
age = 18
#格式化输出--%%输出的就是%；%06d表示输出整数位数为6，不足补0，超过6位有多少显示多少；
# %.02f表示小数点后保留两位
print("我叫%s,今年%d啦" % (name,age))
percent = 99
print("完成了%d%%的工作量" % percent)
#获取变量类型
print(type(name))
#字符串变量计算
print("name"*2)
#拼接字符串
gender = "man"
print(name+gender)
#input函数 ：获取用户通过键盘输入的内容，用户输入的任何内容都记录为字符串
money = input("请输入一个数据用于测试input函数，获取键盘输入数据： ")
print("刚才输入的内容是: %s" %money)
money = float(input("输入一个数值直接转换为浮点型： "))
#类型转换
print(type(money))
print(type(int(money)))



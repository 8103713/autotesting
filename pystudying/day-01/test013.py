#coding:utf-8
"""break和continue"""
i = 0
j = 0
s = 0
n = 0
while(i<100):
    s += i
    i += 1
    if(i > 10):
        print("用break退出时，变量i的值为: %d" % i)
        break
    print("测试i的值为：%d" % i)
print("当i大于10时，s的值为:%d" % s)

#使用continue要注意计数器的位置
while(j<10):
    j += 1
    if (j == 5):
        print("5这个数跳过，如果成功最后和应该为50")
        continue
    #print(j)
    n += j

print("1到10不加5的和为： %d" % n)

#打印五排小星星
a = 0
while(a<6):
    print("*"*a)
    a += 1

#打印九九乘法表
row = 1
while(row <= 9):
    col = 1
    while(col <= row ):
        print("%d*%d=%d" %(col, row, col*row),end="\t")
        col += 1
    print()
    row += 1





#coding:utf-8
"""while使用"""
#程序计数一般从0开始
i = 0
sum = 0
while(i < 101):
    sum += i
    i += 1
print("0到100的和为： %d" % sum)

j = 0
result = 0
while( j % 2 == 0 and j <= 100 ):
    result += j
    j += 2
print("0到100的偶数和为： %d" % result)

k = 1
s = 0
while( k % 2 == 1 and k < 100):
    s += k
    k += 2
print("0到100的奇数和为： %d" % s)

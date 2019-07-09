#coding:utf-8
"""初识函数，定义函数的上方应该与其它代码保留两个空行"""


def mul_table():
    """
    选中函数，pycharm会背景出一个小灯泡，在灯泡中选插入文档字符串
    """
    row = 1
    while (row <= 9):
        col = 1
        while (col <= row):
            print("%d*%d=%d" % (col, row, col * row), end="\t")
            col += 1
        print()
        row += 1
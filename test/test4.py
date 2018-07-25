# -*- coding: utf-8 -*-
'''
获取训练集天数
'''
import datetime
import numpy as np


def getdate(n):
    date = str(datetime.datetime.now() + datetime.timedelta(days=n))[0:10]
    return date


x1 = []
x2 = []
x3 = []
x4 = []
x5 = []
x6 = []
x7 = []
x8 = []
x9 = []
y = []

x7.append((getdate(-31) + ' 21'))
x7.append((getdate(-31) + ' 22'))
x7.append((getdate(-31) + ' 23'))
x8.append((getdate(-31) + ' 22'))
x8.append((getdate(-31) + ' 23'))
x9.append((getdate(-31) + ' 23'))
for i1 in range(30):
    for i2 in range(24):
        x1.append(getdate(-51 + i1) + (" %02d" % i2))
        x2.append(getdate(-44 + i1) + (" %02d" % i2))
        x3.append(getdate(-37 + i1) + (" %02d" % i2))
        x4.append(getdate(-33 + i1) + (" %02d" % i2))
        x5.append(getdate(-32 + i1) + (" %02d" % i2))
        x6.append(getdate(-31 + i1) + (" %02d" % i2))
        x7.append(getdate(-30 + i1) + (" %02d" % i2))
        x8.append(getdate(-30 + i1) + (" %02d" % i2))
        x9.append(getdate(-30 + i1) + (" %02d" % i2))
        y.append(getdate(-30 + i1) + (" %02d" % i2))
x7.pop()
x7.pop()
x7.pop()
x8.pop()
x8.pop()
x9.pop()
# print(x1)
# print(x2)
# print(x3)
# print(x4)
# print(x5)
# print(x6)
# print(x7)
# print(x8)
# print(x9)
# print(y)


# X = np.vstack((x1, x2, x3, x4, x5, x6, x7, x8, x9)).T
# print(X[-1])
# print(len(X))
Y = np.array(y).T
print(Y[-1])

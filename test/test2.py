# -*- coding: utf-8 -*-
import time

## dd/mm/yyyy格式
# a=time.strftime("%d")
# print(type(a))
a = time.strftime("%H:%M:%S")
print(a)
while True:
    current_time = time.localtime(time.time())
    if (current_time.tm_hour == 15) and (current_time.tm_min == 29) and (current_time.tm_sec == 0):
        print("hello")
        break

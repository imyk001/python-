#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#--1定义列表
#

a = int(input('请输入一个数字：'))
if a in range(90,100):
    print('A')
elif a in range(80,90):
    print('B')
elif a in range(70,80):
    print('C')
elif a in range(60,70):
    print('D')
else:
    print('E')
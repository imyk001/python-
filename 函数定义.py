#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
def add(a,b):
    return (int(a)+int(b))

a,b = input('输入两个数字并用逗号隔开:',).split(',')
#函数的调用
print(add(a,b))
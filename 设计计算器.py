#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
def add(a,b):
    print(int(a)+int(b))
def jianfa(a,b):
    print(int(a)-int(b))
def cheng(a,b):
    print(int(a)*int(b))
def chu(a,b):
    if int(b) ==0:
        print('请输入非0参数')
    else:
        print(int(a)/int(b))
a,b =input('请输入两个数字并用逗号隔开:',).split(',')
k = input('请输入运算符：',)
if k =='+':
    add(a,b)
elif k =='-':
    jianfa(a,b)
elif k =='*':
    cheng(a,b)
else:
    chu(a,b)


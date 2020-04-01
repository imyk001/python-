#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
def calc(a,b):
    try:
        print(int(a)/int(b))
    except ZeroDivisionError as result:
        print(result)
    else:
        print('无异常')
    finally:
        print('程序执行结束')
a,b = input('输入a,b：',).split(',')
calc(a,b)
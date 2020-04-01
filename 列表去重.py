#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
list =[1,2,3,4,3,4,2,5,5,8,9,7]
list.sort()
l1 = []
i = 1
print(list)
for i in list:
    if i not in l1:
        l1.append(i)
print(l1)


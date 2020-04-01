#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
l = []
for i in range(0,10):
    if i ==0 or i ==1:
        l.append(i)
    else:
        l.append(l[i-2]+l[i-1])
print(l)
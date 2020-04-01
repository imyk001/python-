#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
l = []
for i in range(2,101):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        l.append(i)
print(l)


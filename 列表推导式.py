#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
# list =[i for i in range(1,11)]
# print(list)
# l1 = [i**2 for i in range(1,11) ]
# print(l1)
# l2 = [i**2 for i in range(1,11) if i%2==0]
# print(l2)
# l = [[1,2,3],[4,5,6],[7,8,9],[10]]
# l1=[]
# for i in l:
#     for j in i:
#         if j%2==0:
#            l1.append(j**2)
# print(l1)
# for i in l:
#     for j in i:
#         if len(i)>1 and j%2==0:
#             l1.append(j**2)
# print(l1)

l = [i for i in range(0,101) if i%2==0 and i%3==0]
print(l)
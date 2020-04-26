#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
"""
需求：
需要设计一个积分榜，按照以下规则
1-10名：加权系数5.0-2.0，
11-30名：加权系数：2.0-1.0
30-60：加权系数：1.0-0
解释：
1-每个名字的积分=每个名次对应的加权系数*1000
2-每个阶段的加权系数按照等差分布，
举例：
1-比如1-10名的加权系数分别为5.0、4.7、4.4、依次递减到2.0
2-第一名的积分=5.0*1000；第二名的积分=4.7*1000
3-积分榜结果=每个阶段的加权系数*1000
题目：请计算以上每个范围的积分结果
"""
def Standings():
    for rank in range(1,61):
        if rank in range(1,11):#1-10名的积分结果
            weightNumberVa = float((rank-1))*(5.0-2.0)/10 #加权系数等差值
            weightNumber = 5.0 - weightNumberVa #加权系数
            score = weightNumber *1000
            print('第%s名的积分为%.2f'%(rank,score))
        elif rank in range(11,31): # 1-10名的积分结果
            weightNumberVa = float((rank - 11)) * (2.0 - 1.0) / 20  # 加权系数等差值
            weightNumber = 2.0 - weightNumberVa  # 加权系数
            score = weightNumber * 1000
            print('第%s名的积分为%.2f' % (rank, score))
        else:
            weightNumberVa = float((rank - 31)) * 1.0 / 30  # 加权系数等差值
            weightNumber = 1.0 - weightNumberVa  # 加权系数
            score = weightNumber * 1000
            print('第%s名的积分为%.2f' % (rank, score))

if __name__ == '__main__':
    Standings()
#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
# 3、通过定制cookie，单独设置cookie来访问目标网址
#1-导包
import requests
#2-登录接口
url = 'https://www.wanandroid.com/user/login'
payload = {'username':'yk4659136','password':'yankai123'}
#3-发送请求
r = requests.post(url=url,data=payload)
print(r.text)
print(r.cookies)
#4-使用上次请求的response中的cookie，通过字典形式用cookie返回的JSESSIONID，放入下次请求的cookie中
cookie = {'JSESSIONID':r.cookies['JSESSIONID']}
#5-携带cookie信息发送请求
r2 = requests.get(url ='https://www.wanandroid.com/lg/todo/list/0',cookies = cookie)
print(r2.text)

#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#1、通过r.cookies手动获取上一请求返回的cookie来设置下次请求的cookie

import requests
#登录接口
urlstr = 'https://www.wanandroid.com/user/login'
#传递参数
payload = {'username':'yk4659136','password':'yankai123'}
#response返回值
r = requests.post(url=urlstr,data = payload)
print('cookies的值：',r.cookies)
print('header：',r.headers)
print('text:',r.text)
# 获取上次登录的cookies的值传递给下次登录
cookie= r.cookies
print(cookie)
urlstr1 = 'https://www.wanandroid.com/lg/todo/list/0'
#携带cookie发送请求
r1 = requests.get(url = urlstr1,cookies =cookie)
print(r1.text)
print(r1.status_code)
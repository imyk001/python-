#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests
url = 'https://www.wanandroid.com/user/login'

payload = {'username':'yk4659136','password':'yankai123'}
#舒适化session对象
s = requests.session()
#通过session对象发送请求#服务器设置在本地的cookie会保存在本地
r = s.post(url = url ,data = payload)
#通过session继续发送post请求，自动携带上一个请求返回的cookie
r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')

print(r.text)
print(r2.text)
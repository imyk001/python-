#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests,json
#请求接口
url = 'https://www.wanandroid.com/user/login'
#请求参数
payload = {"username":"yk4659136","password":"yankai123"}
# json.dumps(payload)
#发送post请求
r = requests.post(url=url,data = payload)
print(r.text)
print(r.status_code)
print(type(payload))
print(type(r.json()))
print(r.json()['data']['nickname'])
print(r.json()['errorCode'])

if r.json()['data']['username']=='yk4659136' and r.status_code ==200:
    print('登录成功')
else:
    print('失败')
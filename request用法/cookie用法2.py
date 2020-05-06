#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#2、通过rquests.session自动设置cookie，来完成访问
import requests
#访问接口
urlstr = 'https://www.wanandroid.com/user/login'
#传递参数
payload = {'username':'yk4659136','password':'yankai123'}
#初始化session对象
s = requests.session()
#使用session登录传递cookie
r = s.post(url = urlstr,data = payload)
#通过session继续发送get请求，自动携带上一个请求返回的cookie
r2 = s.get(url = 'https://www.wanandroid.com/lg/todo/list/0')

print(r2.text)
print(r.text)
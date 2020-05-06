#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
#4、通过定制cookie，放入header来访问目标网址
import requests
#访问接口
urlstr = 'https://www.wanandroid.com/user/login'
#传递参数
payload = {'username':'yk4659136','password':'yankai123'}
#发送请求
r = requests.post(url=urlstr,data=payload)
print('1-------',r.text)
print('2-------',r.cookies)
print('3-------',r.headers)
#获取上次请求放回的response中的cookie，通过字典的形式引用cookie返回的JSESSIONID，放入下次请求的header中
header ={'cookie':'JSESSIONID='+r.cookies['JSESSIONID']}

# 携带header信息请求list接口
r2 = requests.get(url = 'https://www.wanandroid.com/lg/todo/list/0',headers=header)
print(r2.text)
#str.find方法返回-1标识未找到，非-1表示找到
result =r2.text.find('已完成清单')
print(result)
if result !=1:
    print('查询成功')
else:
    print('查询失败')

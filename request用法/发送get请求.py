#!/usr/bin/env python
# enccoding: utf-8
'''
@author: Yankai
@project:
'''
import requests

#发送get请求
urlstr ='https://www.wanandroid.com/'

#参数
payload = {'k':'Android'}
#引用get方法
r = requests.get(url=urlstr,params=payload)
#结果
print(r.text)#字符串方式的响应体，会自动根据响应头部的字符编码进行解码
print(r.content)#字节方式的响应体，会自动为你解码gzip和deflate压缩
print(r.text.encode('utf-8'))
print(r.status_code)#响应状态码
print(r.url)#获取url
print(r.encoding)#编码格式
print(r.cookies)#获取response返回的cookie
print(r.raw)#返回原始响应体
print(r.json)#request中内容json解码器，处理后对应python
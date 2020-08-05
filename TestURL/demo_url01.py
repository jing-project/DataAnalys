# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:  2020-08-05下午 4:05
# 开发工具:PyCharm
import urllib.request
# 获取get的请求
# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.read().decode('utf-8'))#对获取到的网页源码进行utf-8进行解码

# 获取post的请求 模拟用户真实登录
# import urllib.parse
# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# response = urllib.request.urlopen('http://httpbin.org/post',data)
# # print(response.read())
# print(response.read().decode('utf-8'))


# import urllib.error
# # 超时处理
# try:
#     response = urllib.request.urlopen('http://httpbin.org/get',timeout=0.1)
#     # print(response.read())
#     print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print('time out!')


# response = urllib.request.urlopen('http://www.baidu.com')
# print(response.status,response.getheader())

# 解决发现为爬虫 伪装浏览器
# import urllib.parse
# url = 'https://httpbin.org/post'
#
# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding='utf-8')
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
# req = urllib.request.Request(url=url,data=data,headers=headers,method='POST')
#
# response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))


url = 'https://www.douban.com'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
req = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
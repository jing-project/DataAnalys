# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:  2020-08-05下午 5:05
# 开发工具:PyCharm
'''
解析网页

# BeautifulSoup4 将复杂HTML文档转换成一个复杂的树形结构，每个节点都是python对象，所有对象可以归纳为4种
-Tag
-NavigableString
-BeautifulSoup
-Comment
'''
from bs4 import BeautifulSoup
import urllib.request
import re
url = 'https://www.baidu.com'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
req = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(req)
# print(response.read().decode('utf-8'))

html = response.read().decode('utf-8')

bs = BeautifulSoup(html,'html.parser')
# print(bs.title)
# print(bs.a)
#
# # 1 Tag 标签及其内容
# print(type(bs.a))
# print(bs.title.string)
# # 2 NvigableString 标签里的内容
# print(type(bs.title.string))
#
# # 3 BeautifulSoup 表示整个一文档
# print(bs)
# print(type(bs))
# print(bs.name)
#
# print(bs)
#
#
# # 4 Comment 是一个特殊的NavigabelString，输出的内容不包含注释符号
# print(bs.a.string)
# print(type(bs.a.string))


#---------------------------------------------------------
# 文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])
# # 文档的搜素
# #（1） find_all 字符串查找，会查找与字符串完全匹配的内容
# t_list = bs.find_all('a')
# print(t_list)
# # （2）正则表达式搜素：使用search（）方法来匹配内容
# t_list2 = bs.find_all(re.compile('a'))
# print(t_list2)
#
# # 方法：传入一个函数，根据函数的要求来搜素
# def name_is_exists(tag):
#     return tag.has_attr('name')
# t_list3 = bs.find_all(name_is_exists)


# # 2 参数
# t_list = bs.find_all(id = 'head')
# for item in t_list:
#     print(item)
# 3 text 参数
# # t_list = bs.find_all(text = '百度一下，你就知道')
# t_list = bs.find_all(text = re.compile('\d'))#特定文本的的内容
# for item in t_list:
#     print(item)
# # 4 limit
# # t_list = bs.find_all(text = '百度一下，你就知道')
# t_list = bs.find_all('a',limit=3)#特定文本的的内容
# for item in t_list:
#     print(item)

# css 选择器
# t_list = bs.select('title')#通过标签来查找
# t_list = bs.select('.mnav')##通过类名来查找
t_list = bs.select('#u1')##通过id来查找
for item in t_list:
    print(item)

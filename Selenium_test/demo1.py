# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:上午 11:04
# 开发工具:PyCharm
from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
# import time
# 打开浏览器
b = webdriver.Firefox()

#  打开网页
html = b.get('http://www.baidu.com')
# print(html)
sleep(3)
# 查找元素
ele = b.find_element_by_id('kw').send_keys('selenium')
print(ele)
b.find_element_by_id('su').click()

# 退出
# b.quit()

# soup = BeautifulSoup(html,'lxml')
# print(soup.title)
# print()
# print(b.current_url)



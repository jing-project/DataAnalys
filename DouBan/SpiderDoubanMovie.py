# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:  2020-08-05下午 3:47
# 开发工具:PyCharm

from bs4 import BeautifulSoup#网页解析，获取数据
import re #正则表达式，进行文字匹配
import  urllib.request,urllib.error #指定url，获取网页数据
import xlwt #进行excel操作
import sqlite3 #进行SQLite数据库操作



def main():
    baseURL = 'http://movie.douban.com/top250?start='

    # 1.爬取网页
    dataList = getData(baseURL)
    # 2.解析数据

    # savepath = './豆瓣电影Top250.xls'
    # # 3.保存数据
    # saveData(savepath)

    askURL(baseURL)
# 爬取网页
def getData(baseurl):
    dataList = []
    for i in range(0,10):

        url = baseurl + str(i*25)#调用获取页面信息的函数10次
        html = askURL(url)#保存获取到的网页源码
        # 2 逐一解析网页

    return dataList
# 得到指定一个网页内容
def askURL(url):

    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}
    req = urllib.request.Request(url=url, headers=head)
    html = ''
    try:
        response = urllib.request.urlopen(req)
        html = response.read().decode('utf-8')
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e,'code'):
            print(e.code)
        if hasattr(e,'reason'):
            print(e.reason)
    return  html
# 保存数据
def saveData(savepath):
    print('save......')

if __name__ == '__main__':

    main()
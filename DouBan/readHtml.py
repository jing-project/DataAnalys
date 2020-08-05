# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:  2020-08-05下午 7:14
# 开发工具:PyCharm
import re
from bs4 import BeautifulSoup
import re

# 影片详情连接的规则
findLink = re.compile(r'<a href="(.*?)">')#创建正则表达式对象，表示规则
# 影片图片

# 影片的片名
findTitle = re.compile(r'<span class="title">(.*)</span>')
# 影片的评分
findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
# 评价人数
findJudge = re.compile(r'<span>(\d*)人评价</span>')
# 影片的主演
findActor = re.compile(r'<p class="">(.*?)</p>',re.S)
html = open('./OnePage.html','r',encoding='utf-8')
soup = BeautifulSoup(html,'html.parser')
for item in soup.find_all('div', class_='item'):
    # print(item)#测试：查看电影的item全部信息
    data = []  # 保存一部电影的所有信息
    item = str(item)
    link = re.findall(findLink, item)[0]
    title = re.findall(findTitle, item)
    print(link)
    print(title)
    if len(title)==2:
        ctitle = title[0]
        data.append(ctitle)
        ftitle = title[1].replace('\xa0/\xa0',"")
        data.append(ftitle)
    else:
        data.append(title[0])
        data.append('')
    print(data)
    rate = re.findall(findRating, item)[0]
    print(rate)
    people = re.findall(findJudge, item)[0]
    print(people)
    star = re.findall(findActor, item)[0]
    star = re.sub('<br(s+)?/>(\s+)',"",star)
    star = re.sub('/',"",star)
    star =star.replace('\xa0','')

    data.append(star.strip())
    print(data)
    print(star)
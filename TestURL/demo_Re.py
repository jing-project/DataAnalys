# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:  2020-08-05下午 6:03
# 开发工具:PyCharm
import re
#正则表达式

a = '导演: 彼得·威尔 Peter Weir   主演: 罗宾·威廉姆斯 Robin Williams / 罗伯...1989 / 美国 / 剧情'
sub = a.index('主演')
print(sub)
print(a[sub:])
mh = a[sub:].split(':')[1]  # 得到主演后面的信息
print(re.split('[1-2]+', mh)[0])  # 正则切片得到主演信息
print(re.findall('[0-9]+./.*?/', a)[0])
# '''
#
# # 网址r"\n" =="\\n" 但 r"a\nb"!="a\nb" r的功能则为转义字符 \n 为换行 \\n 表示 \n
# # pattern.match 从字符串第一个字符找，不匹配为空，匹配下一个字符找 ，找一个
# # pattern.searech() 任何位置的整个字符串开始治找一个
# # pattern.findall 找多个
#
#
# '''
#
#
# print(re.findall('.','\n'))#[]
# print(re.findall('.','\n',re.S))#['\n']
# print(re.findall('.','\n',re.DOTALL))#['\n']
#
# print(re.findall("a[bcd]e","abcde"))#[]
# print(re.findall("a[bcd]+e",'abcde'))#['abcde']
#
# print(re.findall('abce|aede|afce','abce'))#['abce']
#
#
# print(re.findall(r"a.*bc","a\nbc",re.DOTALL))#['a\nbc']
# print(re.findall(r"a(.*)bc","a\nbc",re.DOTALL))#['\n']
# str1  ='http://www.baidu.com'
# email = "1210640219@qq.com"
# regular1 = re.compile(r'[0-9a-zA-Z.]+@[0-9a-zA-Z.]+?com')
# regular = re.compile(r'[a-zA-Z.]+://[^\s].*[.com|.cn]]')
# result = re.findall(regular,str1)
# result1 = re.findall(regular1,email)
# print(result1)
# print(result)

arr = "hello world".split(" ")
new_str = f"{arr[0].capitalize()} {arr[1].capitalize()}"
print(new_str)
s1 = 's12412asd'
print(s1.isnumeric())#判断字符串中是否只有数字
s2 = "ilovechina"#进行反转
''.join(reversed(s2))
print(s2[::-1])
print(''.join(reversed(s2)))
papa1 = re.compile(r'[0-9]+')
print(re.findall(papa1,s1))
s3 =  ' adabdw '#,要求写一个函数把这个字符串的前后空格都去掉。
print(len(s3))
print(s3.strip(),len(s3.strip()))
s4 = '123456'
print(s4[-2:])#最后的两个字符。
# s="info：xiaoZhang 33 shandong"，用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
s5 = "info：xiaoZhang 33 shandong"
print(re.findall(r'[^:\s]+', s5))
print(s5.split(' '))

alist = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]
alist.sort(key=lambda x: x['age'])
print(alist)

a = ['apple', 'banana', 'apple', 'tomato', 'orange', 'apple', 'banana', 'watermeton']
dic = {}
for key in a:
     dic[key] = dic.get(key, 0) + 1
print(dic)
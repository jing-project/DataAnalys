# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:  2020-08-05下午 6:03
# 开发工具:PyCharm
import re
#正则表达式
'''

# 网址r"\n" =="\\n" 但 r"a\nb"!="a\nb" r的功能则为转义字符 \n 为换行 \\n 表示 \n
# pattern.match 从字符串第一个字符找，不匹配为空，匹配下一个字符找 ，找一个
# pattern.searech() 任何位置的整个字符串开始治找一个
# pattern.findall 找多个


'''


print(re.findall('.','\n'))#[]
print(re.findall('.','\n',re.S))#['\n']
print(re.findall('.','\n',re.DOTALL))#['\n']

print(re.findall("a[bcd]e","abcde"))#[]
print(re.findall("a[bcd]+e",'abcde'))#['abcde']

print(re.findall('abce|aede|afce','abce'))#['abce']


print(re.findall(r"a.*bc","a\nbc",re.DOTALL))#['a\nbc']
print(re.findall(r"a(.*)bc","a\nbc",re.DOTALL))#['\n']
str1  ='http://www.baidu.com'
email = "1210640219@qq.com"
regular1 = re.compile(r'[0-9a-zA-Z.]+@[0-9a-zA-Z.]+?com')
regular = re.compile(r'[a-zA-Z.]+://[^\s].*[.com|.cn]]')
result = re.findall(regular,str1)
result1 = re.findall(regular1,email)
print(result1)
print(result)
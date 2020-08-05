# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:  2020-08-05下午 3:23
# 开发工具:PyCharm
info = {'name':'吴彦祖','age':18}
# 字典的访问
print(info['name'])
print(info['age'])

#
print(info.get('gender'))
print(info.get('gender','m'))#访问的键不存在时，返回默认值
print(info.keys())
print(info.values())
print(info.items())

for key,value in info.items():
    print('key = %s,value = %s'%(key,value))
c = ['a','e','3',2]
for i,x in enumerate(c):
    print(i,x)
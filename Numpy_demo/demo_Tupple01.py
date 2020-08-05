# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:下午 12:08
# 开发工具:PyCharm
# 元组中的元素不能修改
tup1 = ()
print(type(tup1))
tup2 = (23)
print(type(tup2))
tup3 = (34,)
print(type(tup3))

tup1 = ('python',1997,'hello',2000)
tup2 = (1,2,3,4,5,6,7,8,9,10)
# tup1[0] = '1213'不支持修改
# tup1 = ('12')
print('tupple[0]:',tup1[0])
print('tupple[0:3]:',tup1[0:3])
print('tupple[0]:',tup2[0])
print('tupple[:-1]:',tup2[:-1])
tup = tup1+tup2
print(tup)
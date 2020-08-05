# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:上午 11:35
# 开发工具:PyCharm
# 列表中的元素的类型可以不相同，支持数字，字符串，也可包含列表
# nameList  = []#定义一个空的列表

nameList  = ['小张','小王','小李']
# testList = [1,'测试']
#
# print(type(nameList[0]),nameList[0])
# print(type(testList[0]))
length = len(nameList)
# print(len(nameList))#获得列表长度
# for name in nameList:
#     print(name)
# i = 0
# while i<length:
#     print(nameList[i])
#     i = i +1
#
# 增  [append] [extend] [insert]
# print("----------增加前，列表数据------------")
# for name in nameList:
#     print(name)
#
#
# nameTemp = input('请输入添加学生的姓名：')
# 1 append
# nameList.append(nameTemp)#在末尾追加一个元素
# print("----------增加后，列表数据------------")
# for name in nameList:
#     print(name)
a = [1,2,]
b  = [3,4]
a.append(b)
print(a)
# 2 extend
a.extend(b)#将吧列表的每个元素，注意追加到啊列表中
print(a)
# 3 insert
a.insert(1,3)#第一个变量表示下标，第二个表示元素（对象）
print(a)

# 删 [del] [pop] [remove]
print(a)
del a[0]#在指定位置删除一个元素
print(a)

a.pop()#删除末尾最后一个元素
print(a)

a.remove(3)#删除指定内容的元素
print(a)

# 改
a[0] = 9# 指定位置的更改元素内容
print(a)

# 查 in index count

num = input('请输入要查找的数字：')
if num in a :
    print('找到了')
else:
    print('没有找到')

print(a.index(3,0,3))#可以查找指定下标范围的元素，并返回找到对应数据的下标范围区间，左闭右开[0, 3)

print(a.count(3))#返回查找元素出现的次数

c = [1,2,3,4]

print(c)
c.reverse()
print(c)
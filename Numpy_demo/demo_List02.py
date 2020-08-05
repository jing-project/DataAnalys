# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:2020/8/5 0005} 下午 12:20}  2020-08-05 

# 开发工具:PyCharm
import random
offices = [[],[],[]]
names = ['A','B','C','D','E','F','G','H']
for name in names:
    index = random.randint(0,2)
    offices[index].append(name)
i =1
for office in offices:
    print("办公室%d的人数为：%d"%(i,len(office)))
    i = i+1
    for name in office:
        print(name,end='\t')
    print('\n')
    print('-'*20)
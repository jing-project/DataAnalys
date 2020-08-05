# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:下午 12:00
# 开发工具:PyCharm
# 散点图
# 北京2016.3月和10月每天白天的最高气温，找出规律
from matplotlib import pyplot as plt

# 设置字体中文出现错误
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

y_3 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]

y_10 = [26,26,28,19,21,17,16,19,18,20,19,22,23,17,20,20,21,21,22,15,11,15,5,13,17,10,11,13,12,13,6]

# print(len(y_10))
# print(len(y_3))

x_3 = range(1,32)
x_10 = range(51,82)

# 设置图像大小
plt.figure(figsize=(20,8),dpi = 80)
# 使用 Scatter方法绘制散点图
plt.scatter(x_3,y_3,label = '3月份')
plt.scatter(x_10,y_10,label='10月份')

# 调整X轴的刻度
_x = list(x_3)+list(x_10)
_xtick_labels = ["3月{}日".format(i) for i in x_3]
_xtick_labels += ["10月{}日".format(i-50)for i in x_10]


plt.xticks(_x[::3],_xtick_labels)

# 添加图例
plt.legend(loc='upper left')

# 添加描述信息
plt.xlabel("时间")
plt.ylabel("温度")
plt.title('3和10月份的温度变化')
plt.show()





# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:上午 11:58
# 开发工具:PyCharm

# matplotlib 数据可视化

# 假设一天中每个两个小时（range(2,26,2)）的气温分别是[15,13,14.5,17,20,25,26,26,27,22,18,15]
from matplotlib import pyplot as plt

from matplotlib import font_manager

x = range(2,26,2)
y = [15,13,14.5,17,20,25,26,26,27,22,18,15]
# 设置图像大小
fig = plt.figure(figsize=(20,8),dpi = 80)
# 绘图
plt.plot(x,y)
# 设置x轴的刻度和属性
plt.xticks(x)

# 设置字体中文出现错误
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

# 设置坐标轴的属性
plt.xlabel("时间")
plt.ylabel("温度 单位（°C）")
plt.title('一天的气温变化')
# 保存图像
# plt.savefig('./figure.png')

plt.show()
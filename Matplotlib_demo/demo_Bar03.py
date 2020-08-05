# -*- conding utf-8 -*-
# 作者：彭静
# 开发时间:下午 12:05
# 开发工具:PyCharm
# 条形图 数量统计 频率统计
# 电影在2017-09-14（b_14），2017-09-15（b_15）,2017-09-16(b_16)三天的票房
# a = ["猩球崛起:终极之战","教刻尔克","蜘蛛侠:英雄归来","战狼2"
# b_16 = [15746,312,4497,319]
# b_15 = [12357,156,2045,168]
# b_14 = [2358,399,2358,362]

from matplotlib import pyplot as plt

# 设置字体中文出现错误
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

a = ["猩球崛起:终极之战","教刻尔克","蜘蛛侠:英雄归来","战狼2"]
b_16 = [15746,312,4497,319]
b_15 = [12357,156,2045,168]
b_14 = [2358,399,2358,362]

bar_width = 0.2
x_14 = list(range(len(a)))
x_15 = [i+bar_width for i in x_14]
x_16 = [i+bar_width*2 for i in x_14]

plt.bar(range(len(a)),b_14,width=bar_width,label = "9月14日")
plt.bar(x_15,b_15,width=bar_width,label = "9月15日")
plt.bar(x_16,b_16,width=bar_width,label = "9月16日")

plt.xticks(x_15,a)

plt.legend()
plt.xlabel("电影")
plt.ylabel("票房（亿元）")
plt.title('3天电影的票房')
plt.show()
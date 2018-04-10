#-*- coding:utf -8-*-

import matplotlib.pyplot as plt


x_values = list(xrange(1, 100))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, edgecolor='none', s=40)
# 设置图表标题,并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)  # x轴标题
plt.ylabel('Square of Value', fontsize=14)  # y轴...

# 设置每个坐标轴的取值范围
plt.axis([0, 100, 0, 10000])  # x和y坐标轴的最小值和最大值

plt.show()

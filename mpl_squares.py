#-*- coding:utf -8-*-

import matplotlib.pyplot as plt


x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.scatter(x_values, y_values, s=100)  # s为点的尺寸
# 设置图表标题,并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)  # x轴标题
plt.ylabel('Square of Value', fontsize=14)  # y轴...

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

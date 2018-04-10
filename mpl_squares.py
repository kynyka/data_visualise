#-*- coding:utf -8-*-

import matplotlib.pyplot as plt


input_values = [1, 2, 3, 4, 5]  # 指定plot()的输入值;默认是第一个数据点的x坐标值为0
squares = [1, 4, 6, 16, 25]
plt.plot(input_values, squares, linewidth=5)  # 设置输入值/输出值/绘制线条的粗细

# 设置图表标题,并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)  # x轴标题
plt.ylabel('Square of Value', fontsize=14)  # y轴...

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()

#-*- coding:utf -8-*-

import matplotlib.pyplot as plt


squares = [1, 4, 6, 16, 25]
plt.plot(squares, linewidth=5)  # 设置绘制线条的粗细

# 设置图表标题,并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)  # x轴标题
plt.ylabel('Square of Value', fontsize=14)  # y轴...

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()

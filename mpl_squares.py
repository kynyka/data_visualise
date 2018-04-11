#-*- coding:utf -8-*-

import matplotlib.pyplot as plt


x_values = list(xrange(1, 100))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)  # 自定义颜色可如c=(0,0,0.8)般RGB表示,但此中每个数须为0~1之间;越近0颜色越深,近1则浅; 颜色映射,让线条有浅深变化;matplotlib的所有颜色映射见官网Examples>>colormas_reference
# 设置图表标题,并给坐标轴加上标签
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)  # x轴标题
plt.ylabel('Square of Value', fontsize=14)  # y轴...

# 设置每个坐标轴的取值范围
plt.axis([0, 100, 0, 10000])  # x和y坐标轴的最小值和最大值

plt.savefig('squares_plot.png', bbox_inches='tight')  # savefig替换show,自动保存图表为文件,路径为本py文件同级目录;第二个实参制定将图表多余空白区域裁减掉,要保留空白区域则可省略此实参。

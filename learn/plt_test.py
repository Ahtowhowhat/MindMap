# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。

# import json
# path = '神经网络模型.json'
# with open(path, 'r', encoding='UTF8') as f:
#     data = json.load(f)

import matplotlib.pyplot as plt
import random
from pylab import mpl

# 设置显示中文字体
mpl.rcParams["font.sans-serif"] = ['SimHei']
# 设置正常显示符号
mpl.rcParams["axes.unicode_minus"] = False

# # 0.准备数据
# x = range(60)
# y = [random.uniform(15, 18) for i in x]  # random.uniform:返回一个随机浮点数 N ，当 a <= b 时 a <= N <= b ，当 b < a 时 b <= N <= a
#
# '''
# DPI（Dots Per Inch，每英寸点数）是一个量度单位，用于点阵数码影像，指每一英寸长度中，取样、可显示或输出点的数目。
# DPI是打印机、鼠标等设备分辨率的度量单位。是衡量打印机打印精度的主要参数之一，一般来说，DPI值越高，表明打印机的打印精度越高。
# '''
# # 1.创建画布
# fig = plt.figure(figsize=(15, 8), dpi=100)  # 画布大小，dpi：清晰度
#
# # 2.绘制图像（折线图）
# plt.plot(x, y)
#
# # 2.1 添加x，y轴刻度
# x_ticks_label = ['11点{}分'.format(i) for i in x]
# y_ticks = range(40)
#
# # 修改x，y轴刻度显示
# # plt.xticks(x_ticks_label[::5])  坐标刻度不可以直接通过字符串进行修改
# # tick：对号; 钩号; 记号
# plt.xticks(x[::5], x_ticks_label[::5])  # 先修改为数字刻度，之后替换中文刻度
# plt.yticks(y_ticks[::5])
#
# # 2.2 添加网格显示
# plt.grid(True, linestyle='--', alpha=0.5)
#
# # 2.3 添加描述信息
# plt.xlabel('时间')
# plt.ylabel('温度')
# plt.title('中午11点-12点某城市温度变化图', fontsize=20)
#
# # 2.4 图像保存（放在show前面，show()会释放figure资源，如果显示图像之后保存图片只能保存空图片）
# # fig.savefig('./test.png')
#
# # 3.图像显示
# plt.show()

from matplotlib.patches import BoxStyle
import matplotlib
matplotlib.use('Agg')

fig = plt.figure(figsize=(15, 8), dpi=100)  # 画布大小，dpi：清晰度
ax = fig.add_axes([0, 0, 1, 1])

# boxstyle = BoxStyle("round", pad=0.3)
props = {'boxstyle': "round,pad=0.3",
         'facecolor': 'white',
         'linestyle': 'solid',
         'linewidth': 1,
         'edgecolor': 'black'}

t = ax.text(0.5, 0.5, 'hfa',
            horizontalalignment='center',
            verticalalignment='center',
            fontsize=22, color='black',
            fontweight='heavy',
            # fontfamily='SimHei',
            transform=ax.transAxes,
            # bbox=dict(facecolor='red', alpha=0.5, boxstyle='square,pad=0.4')
            bbox=props
            )
# t.set_bbox(dict(facecolor='red', alpha=0.5))


transf = ax.transData.inverted()

# bb = t.get_window_extent(renderer=fig.canvas.renderer)
# # print(bb)
# print(bb.transformed(transf).width,
#       bb.transformed(transf).height)

plt.draw()


print(t.get_bbox_patch().get_bbox().transformed(transf).width,
      t.get_bbox_patch().get_bbox().transformed(transf).height)
print(t.get_bbox_patch().get_extents().transformed(transf).width,
      t.get_bbox_patch().get_extents().transformed(transf).height)
print(type(t.get_bbox_patch().get_bbox()))

# bb = t.get_window_extent(renderer=fig.canvas.renderer)
# # print(bb)
# print(bb.transformed(transf).width,
#       bb.transformed(transf).height)
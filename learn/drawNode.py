import matplotlib.pyplot as plt
import matplotlib.patches as patches

figsize = (16, 9)
dpi = 100
fontsize = 20
text = '神经网络模型'
link_point_parent = (0.5, 0.5)
num_of_child = 4
total_lines = 7
lines_per_child = [3, 2, 1, 1]

# parameters of a rectangle which represents the bounding box of the text
height = (fontsize * 2.0) / figsize[1] / dpi
width = (fontsize * len(text) * 1.5) / figsize[0] / dpi
centerX, centerY = link_point_parent[0] + width / 2, link_point_parent[1]
left, bottom = link_point_parent[0], link_point_parent[1] - height / 2
right, top = link_point_parent[0] + width, link_point_parent[1] + height / 2

# fig
# axes coordinates: (0, 0) is bottom left and (1, 1) is upper right
fig = plt.figure(figsize=figsize, dpi=dpi)
ax = fig.add_axes([0, 0, 1, 1])

# draw the rectangle in axes coords
p = patches.Rectangle(
    (left, bottom), width, height,
    fill=False, transform=ax.transAxes, clip_on=False
)
ax.add_patch(p)

# draw text
ax.text(centerX, centerY, text,
        horizontalalignment='center',
        verticalalignment='center',
        fontsize=fontsize, color='black',
        fontweight='heavy',
        fontfamily='SimHei',
        transform=ax.transAxes)


# draw the trunk and branches
def draw_branch(point, length=0.01):
    """
    draw the link-line to the child \n
    :param point: the position on the trunk
    :param length: the length of branch
    :return: None
    """
    x = (point[0], point[0]+length)
    y = (point[1], point[1])
    ax.plot(x, y,
            transform=ax.transAxes)

# draw_branch((right, centerY))




link_right = (left + width, centerY)

ax.scatter((link_point_parent[0], link_right[0]), (link_point_parent[1], link_right[1]),
           transform=ax.transAxes)

ax.set_axis_off()
plt.show()

# ax.text(left, bottom, 'left top',
#         horizontalalignment='left',
#         verticalalignment='top',
#         transform=ax.transAxes)
#
# ax.text(left, bottom, 'left bottom',
#         horizontalalignment='left',
#         verticalalignment='bottom',
#         transform=ax.transAxes)
#
# ax.text(right, top, 'right bottom',
#         horizontalalignment='right',
#         verticalalignment='bottom',
#         transform=ax.transAxes)
#
# ax.text(right, top, 'right top',
#         horizontalalignment='right',
#         verticalalignment='top',
#         transform=ax.transAxes)
#
# ax.text(right, bottom, 'center top',
#         horizontalalignment='center',
#         verticalalignment='top',
#         transform=ax.transAxes)
#
# ax.text(left, 0.5*(bottom+top), 'right center',
#         horizontalalignment='right',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
#
# ax.text(left, 0.5*(bottom+top), 'left center',
#         horizontalalignment='left',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
#
# ax.text(right, 0.5*(bottom+top), 'centered',
#         horizontalalignment='center',
#         verticalalignment='center',
#         rotation='vertical',
#         transform=ax.transAxes)
#
# ax.text(left, top, 'rotated\nwith newlines',
#         horizontalalignment='center',
#         verticalalignment='center',
#         rotation=45,
#         transform=ax.transAxes)
